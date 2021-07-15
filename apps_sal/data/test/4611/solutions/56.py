# -*- coding: utf-8 -*-
"""
Created on Mon Sep 21 23:53:42 2020

@author: liang
"""

N = int(input())

prev = (0, 0, 0)

flag = True

for i in range(N):
    t, x, y = map(int, input().split())
    if t%2 != (x+y)%2:
        flag = False
    if abs(x+y - prev[1] - prev[2]) > t-prev[0]:
        flag = False
    prev = (t,x,y)

if flag:
    print("Yes")
else:
    print("No")
