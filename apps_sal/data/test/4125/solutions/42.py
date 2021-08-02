# -*- coding: utf-8 -*-
"""
Created on Tue Sep 15 01:58:46 2020

@author: liang
"""

from math import gcd

N, X = map(int, input().split())
A = [abs(int(x) - X) for x in input().split()]

ans = A[0]
for i in range(N):
    ans = gcd(ans, A[i])
print(ans)
