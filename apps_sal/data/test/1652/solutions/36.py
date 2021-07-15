# -*- coding: utf-8 -*-
#ARC65C
import copy
import sys
#import math

hoge = input()
n = len(hoge)

while(1):
	n = len(hoge)
	if(n==0):
		print("YES")
		return
	if(n<=4):
		print("NO")
		return
	else:
		if(hoge[-5:]=="dream"):
			tmp=copy.copy(hoge[0:-5])
			hoge=tmp
		elif(hoge[-5:]=="erase"):
			tmp=copy.copy(hoge[0:-5])
			hoge=tmp
		elif(n<=5):
			print("NO")
			return
		else:
			if(hoge[-6:]=="eraser"):
				tmp=copy.copy(hoge[0:-6])
				hoge=tmp
			elif(n<=6):
				print("NO")
				return
			else:
				if(hoge[-7:]=="dreamer"):
					tmp=copy.copy(hoge[0:-7])
					hoge=tmp
				else:
					print("NO")
					return
	
	

