#!/usr/bin/env	python
#-*-coding:utf-8 -*-
import sys,io,os,math,copy,pickle
d,k,a,b,t=list(map(int,input().split()))
if d<=k:
	print(a*d)
	return
s=a*k
d-=k
if t+s>b*k:
	print(s+b*d)
	return
s+=d//k*(t+s)
d%=k
print(s+min(b*d,t+a*d))

