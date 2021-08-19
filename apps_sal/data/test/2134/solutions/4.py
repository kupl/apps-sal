# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 1/9/20

"""

import collections
import time
import os
import sys
import bisect
import heapq
from typing import List


def issub(u, v):
    if u > v:
        return False
    if u == v:
        return True

    b = 1
    for i in range(v.bit_length() + 1):
        if v & b < u & b:
            return False
        b <<= 1
    return True


def solve(N, A, B):
    vi = collections.defaultdict(list)
    for i, v in enumerate(A):
        vi[v].append(i)

    wc = collections.Counter(A)
    group = {k for k, v in wc.items() if v > 1}
    others = {u for u in wc.keys() if u not in group and any(issub(u, v) for v in group)}
    group |= others

    ans = 0
    for u in group:
        ans += sum([B[i] for i in vi[u]])

    return ans


# def test():
#     N = 7000
#     import random
#     A = [random.randint(1, 10000) for i in range(N)]
#     B = [random.randint(0, 10**9) for _ in range(N)]
#     t0 = time.time()
#     print(solve(N, A, B))
#     print(time.time() - t0)
#
# test()
#
N = int(input())
A = [int(x) for x in input().split()]
B = [int(x) for x in input().split()]
print(solve(N, A, B))
