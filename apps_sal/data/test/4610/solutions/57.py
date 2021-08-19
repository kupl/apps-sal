# -*- coding: utf-8 -*-
"""
Created on Wed Sep 23 15:50:08 2020

@author: liang
"""

N, K = map(int, input().split())
d = [0] * N
A = [int(x) for x in input().split()]

for a in A:
    d[a - 1] += 1

d.sort(reverse=True)

ans = N - sum(d[:K])

print(ans)
