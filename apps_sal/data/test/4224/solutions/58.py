# -*- coding: utf-8 -*-
"""
Created on Fri Sep 18 10:08:18 2020

@author: liang
"""
N = int(input())
A = [int(x) for x in input().split()]
ans = 0
for a in A:
    while a % 2 == 0:
        a //= 2
        ans += 1
print(ans)
