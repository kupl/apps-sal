# -*- coding: utf-8 -*-
"""
Created on Wed Sep  9 01:21:53 2020

@author: liang
"""

A, B, X = map(int, input().split())

for i in range(1, 11):
    if A * 10**(i - 1) + B * i > X:
        i -= 1
        break
ans = (X - B * i) // A
if ans >= 10**9:
    ans = 10**9
if ans >= 10**i:
    ans = 10**i - 1
print(ans)
