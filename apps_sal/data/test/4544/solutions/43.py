# -*- coding: utf-8 -*-
"""
Created on Mon Sep 21 23:37:30 2020

@author: liang
"""

N = int(input())

A = [int(x) for x in input().split()]

d = [0] * (10**5 + 1)

for a in A:
    if a - 1 >= 0:
        d[a - 1] += 1
    d[a] += 1
    d[a + 1] += 1

ans = max(d)

print(ans)
