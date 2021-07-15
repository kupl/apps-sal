# -*- coding: utf-8 -*-
"""
Created on Thu Sep 17 01:45:21 2020

@author: liang
"""

N, K = list(map(int, input().split()))
A = [0]+[int(x) for x in input().split()] + [0]

ans = 0
j = 0
tmp = 0
for i in range(1,N+1):
    tmp -= A[i-1]
    while tmp >= K and i < j:
        tmp -= A[j]
        j -= 1
    while tmp < K and j <= N:
        j += 1
        tmp += A[j]
    ans += N+1 - j
print(ans)

