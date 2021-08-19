# -*- coding: utf-8 -*-
"""
Created on Mon Sep  7 22:29:36 2020

@author: liang
"""
N, K = map(int, input().split())

P = [1 + (int(p) - 1) * 0.5 for p in input().split()]
# print(P)

tmp = sum(P[:K])
ans = tmp
for i in range(N - K):
    tmp += P[K + i] - P[i]
    if tmp > ans:
        ans = tmp

print(ans)
