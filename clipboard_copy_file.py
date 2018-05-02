#!python
#coding:utf-8

import pyperclip
import time
import os,shutil

from urllib import unquote

def clipboard():
	content = ''
	while True:
		spam = pyperclip.paste()
		print('剪贴板内容为：'+spam)
		print('content内容为：'+content)
		if spam!=content:
			if spam[0:4]=='file':
				copyFile(spam[7:],'/home/zhangwei/photo/')
				content = spam
		time.sleep(1)
	return spam

def copyFile(source,targetPath):
	print(source)
	print(targetPath)
	sourcePath = os.path.basename(os.path.dirname(source))
	filename = os.path.basename(source)
	targetPath = unquote(targetPath+sourcePath)
	# 判断路径是否存在
	# 存在     True
	# 不存在   False
	isExists = os.path.exists(targetPath)
	# 判断结果
	if not isExists:
		# 如果不存在则创建目录
		# 创建目录操作函数
		os.makedirs(targetPath) 
		print targetPath + ' 目录创建成功！！！'
	print(targetPath+"/"+filename)
	target = targetPath+"/"+filename
	print('start copy file...')
	print(unquote(source))
	shutil.copyfile(unquote(source),target)

if __name__ == "__main__":
	print(clipboard())
	print(copyFile())
