# -*- coding: utf-8 -*-
"""
Created on Sun Sep 27 02:27:51 2020

@author: liang
"""

N = int(input())
A = [int(x) for x in input().split()]

tmp = sum(A)
tmp -= 2 * A[0]
ans = abs(tmp)
for i in range(1, N - 1):
    tmp -= 2 * A[i]
    ans = min(abs(tmp), abs(ans))
print(ans)
