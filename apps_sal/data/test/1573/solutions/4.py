3
# -*- coding: <utf-8> -*-

import itertools as ittls
from collections import Counter

def sqr(x):
    return x*x

def inputarray(func = int):
    return list(map(func, input().split()))

# -------------------------------
# -------------------------------

N, d = list(map(int, input().split()))

A = [(None, None)]*N
for i in range(N):
    A[i] = tuple(map(int, input().split()))

A.sort(key=lambda x: x[0])
prefix = [0] + [None]*len(A)
for i, (money, friendship) in enumerate(A):
    prefix[i + 1] = prefix[i] + friendship

res, i, j = 0, 0, 0
while i < len(A):
    while j < len(A) and A[j][0] < A[i][0] + d:
        j = j + 1

    if prefix[j] - prefix[i] > res:
        res = prefix[j] - prefix[i]

    i = i + 1

print(res)

