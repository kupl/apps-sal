import numpy as np
import statistics
import bisect
from sys import stdin
import sys
import math
from functools import reduce
import functools
import itertools
from collections import deque, Counter, defaultdict
from operator import mul
import copy
# ! /usr/bin/env python
# -*- coding: utf-8 -*-
import heapq
sys.setrecursionlimit(10**6)
# INF =  float("inf")
INF = 10**18
mod = 10**9 + 7
# mod = 998244353

N, K = list(map(int, input().split()))
A = list(map(int, input().split()))


x = np.argsort(list([-abs(x) for x in A]))
B = []
C = []

for xx in x:
    B.append(A[xx])
    C.append(np.sign(A[xx]))

ans = 1
s = 1
flag4 = 0

for i in range(K):
    s *= C[i]

if s < 0:
    p = np.sign(B[K - 1])
    flag1 = 0
    for i in range(K - 1, -1, -1):
        if C[i] == p * (-1):
            idx1 = i
            flag1 = 1
            break

    flag2 = 0
    for i in range(K, N):
        if C[i] == p * (-1):
            idx2 = i
            flag2 = 1
            break

    flag3 = 0
    if flag1 == 1:
        for i in range(K, N):
            if C[i] == p:
                idx3 = i
                flag3 = 1
                break

    if flag1 and flag2 and flag3:
        if abs(B[K - 1]) * abs(B[idx3]) <= abs(B[idx1]) * abs(B[idx2]):
            B[K - 1] = B[idx2]
        else:
            B[idx1] = B[idx3]
    elif flag1 and (not flag2) and flag3:
        B[idx1] = B[idx3]
    elif flag1 and flag2 and (not flag3):
        B[K - 1] = B[idx2]
    elif (not flag1) and flag2:
        B[K - 1] = B[idx2]
    else:
        flag4 = 1

if flag4:
    for i in range(N - 1, N - K - 1, -1):
        ans = (ans * (B[i] % mod)) % mod
else:
    for i in range(K):
        ans = (ans * (B[i] % mod)) % mod

print((ans % mod))
