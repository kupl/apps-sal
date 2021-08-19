# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 2/12/20

"""

import collections
import time
import os
import sys
import bisect
import heapq
from typing import List


def solve(N, A, B):
    p = [0 for _ in range(N + 1)]
    # print(B)
    for i, v in enumerate(B):
        p[v] = i + 1
    # print(p)
    if p[1]:
        i = 2
        while i <= N and p[i] == p[1] + i - 1:
            i += 1

        if p[i - 1] == N:
            j = i
            while j <= N and p[j] <= j - i:
                j += 1
            if j > N:
                return N - i + 1

    return max([p[i] - i + 1 + N for i in range(1, N + 1)])


N = int(input())
A = [int(x) for x in input().split()]
B = [int(x) for x in input().split()]
print(solve(N, A, B))
