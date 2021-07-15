# -*- coding: utf-8 -*-
"""
Created on Mon Sep 21 21:50:38 2020

@author: liang
"""

N = int(input())
A = [int(x) for x in input().split()]
B = [int(x) for x in input().split()]

tmp = sum(A) + B[N-1]
ans = tmp
for i in reversed(range(1,N)):
    tmp -= A[i]
    tmp += B[i-1]
    if ans < tmp:
        ans = tmp
print(ans)
