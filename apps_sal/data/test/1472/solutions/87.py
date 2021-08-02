# -*- coding: utf-8 -*-
"""
Created on Mon Sep  7 15:49:02 2020

@author: liang
"""

N, X, Y = map(int, input().split())
ans = [0] * (N - 1)
for i in range(1, N + 1):
    for j in range(i + 1, N + 1):
        # print(i,j)
        res = min(abs(i - j), abs(X - i) + 1 + abs(Y - j))
        #print(i, j, res)
        ans[res - 1] += 1

for i in ans:
    print(i)
