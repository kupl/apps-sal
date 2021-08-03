# coding:utf-8

import sys
import bisect

SUM_P = [2**x for x in range(0, 31, 2)]
SUM_M = [2**x for x in range(1, 31, 2)]
for i in range(len(SUM_P) - 1):
    SUM_P[i + 1] += SUM_P[i]
for i in range(len(SUM_M) - 1):
    SUM_M[i + 1] += SUM_M[i]


N = int(input())

ret = 0
while N != 0:
    if N > 0:
        idx = bisect.bisect_left(SUM_P, N)
        idx = idx * 2
        N -= 2 ** idx
        ret += 2**idx
    else:
        idx = bisect.bisect_left(SUM_M, abs(N))
        idx = (idx * 2) + 1
        N += 2 ** idx
        ret += 2**idx

print((format(ret, "b")))
