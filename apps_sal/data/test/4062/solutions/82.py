# -*- coding: utf-8 -*-
a,b,c,d=map(int,input().split())
k=[0]*4
k[0]=a*c
k[1]=a*d
k[2]=b*c
k[3]=b*d
m=sorted(k)
print(m[3])
