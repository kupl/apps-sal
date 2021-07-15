# -*- coding: utf-8 -*-
"""
Created on Sat Oct 21 11:00:49 2017

@author: sven
"""
x1,y1=list(map(int,input().split()))
x2,y2=list(map(int,input().split()))

x=max(abs(x2-x1)+1,2)
y=max(abs(y2-y1)+1,2)
print((x+y)*2)

