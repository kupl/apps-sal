#!/usr/bin/env python3
# -*- coding: utf-8 -*-
n=int(input())
d=[]
l,p,t=0,0,0,
for i in range(n):
    d.append(list(map(int,input().split())))
    if d[i][0]==1:
        l+=1
    if d[i][1]==1:
        p+=1
if l<n-l:
    t+=l
else:
    t+=n-l
if p<n-p:
    t+=p
else:
    t+=n-p
print(t)
