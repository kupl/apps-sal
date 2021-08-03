# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 1/7/20

"""

import collections
import time
import os
import sys
import bisect
import heapq
from typing import List


def solve(N, A):

    B = list(sorted(set(A)))
    vi = {v: i for i, v in enumerate(B)}
    A = [vi[v] for v in A]

    wc = collections.defaultdict(int)
    precount = [0 for _ in range(N)]
    for i, v in enumerate(A):
        wc[v] += 1
        precount[i] = wc[v]

    wc = collections.defaultdict(int)
    sufcount = []
    for v in reversed(A):
        wc[v] += 1
        sufcount.append(wc[v])
    sufcount = sufcount[::-1]

    bit = [0 for _ in range(N)]

    def add(index, val):
        while index < N:
            bit[index] += val
            index |= index + 1

    def query(index):
        s = 0
        while index >= 0:
            s += bit[index]
            index = (index & (index + 1)) - 1
        return s

    ans = 0
    for i in range(N - 2, -1, -1):
        v = precount[i]
        add(sufcount[i + 1], 1)
        ans += query(v - 1)

    return ans


N = int(input())
A = [int(x) for x in input().split()]
print(solve(N, A))
