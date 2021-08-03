# -*- coding: utf-8 -*-

import math
import collections
import bisect
import heapq
import time
import random

"""
created by shhuan at 2017/10/6 22:19

"""

t0 = time.time()
a, b, c = list(map(int, input().split()))


def ct(a, b):
    if a > b:
        a, b = b, a
    L = 998244353
    s = 1
    sx = 1
    for k in range(1, a + 1):
        s = s * (a + 1 - k) * (b + 1 - k) // k
        sx += s % L
    return sx


L = 998244353

print(ct(a, b) * ct(a, c) * ct(b, c) % L)

# print(time.time()-t0)

# p = [[0 for _ in range(MAXN)] for _ in range(MAXN)]
# for i in range(1, MAXN):
#     p[i][0] = 1
#     for j in range(1, i+1):
#         p[i][j] = (p[i-1][j-1]+p[i-1][j]) % MOD
# print(time.time() - t0)
# pre = [0] * MAXN
# pre[0] = 1
# for i in range(1, MAXN):
#     pre[i] = (i*pre[i-1]) % MOD
#
#
# def solve(x, y):
#     ans = 0
#     for k in range(min(x, y)+1):
#         d = pre[k]
#         d = (d*p[x][k]) % MOD
#         d = (d*p[y][k]) % MOD
#         ans = (ans+d) % MOD
#
#     return ans
#
# ans = 1
# ans = (ans * solve(a, b)) % MOD
# ans = (ans * solve(b, c)) % MOD
# ans = (ans * solve(a, c)) % MOD
# print(ans)
#
# print(time.time() - t0)
