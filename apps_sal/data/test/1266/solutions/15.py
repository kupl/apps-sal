#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from math import sqrt
from copy import copy
class figure:
    def __init__(self,ras=None,type=None):
        self.ras=copy(ras)
        self.type=type
n=int(input())
x0,y0=map(int,input().split())
sup='NO'
f=[]
for i in range(8):
    d=figure(10**11)
    f.append(d)
for i in range(n):
    teg,x,y=map(str,input().split())
    x,y=int(x),int(y)
    if x==x0:
        if y<y0:
            ras=abs(y-y0)
            if ras<f[0].ras:
                f[0]=figure(ras,teg)
        if y>y0:
            ras=abs(y0-y)
            if ras<f[1].ras:
                f[1]=figure(ras,teg)
    if y==y0:
        if x>x0:
            ras=abs(x-x0)
            if ras<f[2].ras:
                f[2]=figure(ras,teg)
        if x<x0:
            ras=abs(x0-x)
            if ras<f[3].ras:
                f[3]=figure(ras,teg)
    if abs(x-x0)==abs(y-y0):
        if y<y0 and x<x0:
            ras=sqrt(2)*abs(x-x0)
            if ras<f[4].ras:
                f[4]=figure(ras,teg)
        if y<y0 and x>x0:
            ras=sqrt(2)*abs(x-x0)
            if ras<f[5].ras:
                f[5]=figure(ras,teg)
        if y>y0 and x>x0:
            ras=sqrt(2)*abs(x-x0)
            if ras<f[6].ras:
                f[6]=figure(ras,teg)
        if y>y0 and x<x0:
            ras=sqrt(2)*abs(x-x0)
            if ras<f[7].ras:
                f[7]=figure(ras,teg)
for i in range(8):
    if i in [0,1,2,3]:
        if f[i].type=='R' or f[i].type=='Q':
            sup='YES'
    elif i in [4,5,6,7]:
        if f[i].type=='Q' or f[i].type=='B':
            sup='YES'
print(sup)
