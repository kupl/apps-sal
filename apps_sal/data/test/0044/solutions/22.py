#!/usr/bin/env	python
#-*-coding:utf-8 -*-
d,k,a,b,t=list(map(int,input().split()))
if d<=k:
	print(a*d)
	return
s=a*k
d-=k
if b*k<=t+s:
	print(s+b*d)
	return
s+=d//k*(t+s)
d%=k
print(s+min(b*d,t+a*d))

