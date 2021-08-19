# -*- coding: utf-8 -*-
"""
Created on Sun Sep 27 02:58:21 2020

@author: liang
"""

N, M = list(map(int, input().split()))
MOD = 10**9 + 7

if abs(N - M) >= 2:
    ans = 0
else:
    ans = 1
    for i in range(1, N + 1):
        ans *= i
        ans %= MOD

    for i in range(1, M + 1):
        ans *= i
        ans %= MOD

    if N == M:
        ans *= 2
        ans %= MOD
print(ans)
