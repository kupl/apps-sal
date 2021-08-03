# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 1/10/20

LIS

"""

import collections
import time
import os
import sys
import bisect
import heapq
from typing import List


def solve(N, M, A):

    bit = [0 for _ in range(N)]

    def add(index, val):
        while index < N:
            bit[index] = max(bit[index], val)
            index |= index + 1

    def query(index):
        s = 0
        while index >= 0:
            s = max(s, bit[index])
            index = (index & (index + 1)) - 1

        return s

    q = [(v, i) for i, v in enumerate(A)]
    q.sort()

    s = 0
    for v, i in q:
        t = query(i) + 1
        add(i, t)
        s = max(s, t)

    return N - s


N, M = map(int, input().split())
A = []
for i in range(N):
    x, y = input().split()
    A.append(int(x))

print(solve(N, M, A))
