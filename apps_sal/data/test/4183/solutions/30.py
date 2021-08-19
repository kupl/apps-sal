# -*- coding: utf-8 -*-
"""
Created on Sat Sep 26 22:43:32 2020

@author: liang
"""

from math import gcd

N = int(input())
T = [int(input()) for i in range(N)]
ans = 1

for i in range(N):
    ans = ans * T[i] // gcd(ans, T[i])

print(ans)
