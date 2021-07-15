#!/usr/bin/env	python
#-*-coding:utf-8 -*-
n=int(input())
i=j=n>>1
a=1
b=2
for _ in range(n):
	for y in range(n):
		if min(i,j)<=y<=max(i,j):
			c=a
			a+=2
		else:
			c=b
			b+=2
		print(c,end=' 'if n-1>y else'\n')
	i-=1
	j+=1
	if 0>i:i,j=n-2,1

