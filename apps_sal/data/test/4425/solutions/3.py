# -*- coding: utf-8 -*-
"""
Created on Sat Sep 12 23:11:33 2020

@author: liang
"""

N, K = map(int, input().split())
ans = 0
for i in range(1,N+1):
    tmp = i
    count = 0
    while tmp< K:
        count += 1
        tmp *= 2
    ans += 1/2**count
ans /= N
print(ans)
