# -*- coding: utf-8 -*-
"""
Created on Mon Sep 14 01:36:50 2020

@author: liang
"""

S = input()
c0 = 0
c1 = 0
for i in range(len(S)):
    if S[i] == "0":
        c0 += 1
    else:
        c1 += 1
ans = len(S) - abs(c0-c1)
print(ans)
