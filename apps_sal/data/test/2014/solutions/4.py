# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 1/14/20

"""

import collections
import time
import os
import sys
import bisect
import heapq
from typing import List


memo = [0 for _ in range(1005)]


def longestpath(start, graph):
    if memo[start] > 0:
        return memo[start]

    l = 0
    for v in graph[start]:
        l = max(longestpath(v, graph), l)
    memo[start] = l + 1
    return l + 1


def solve_graph(N, K, A, pos):
    # for each u, v if u appears before v in every array, add a link u->v
    g = collections.defaultdict(list)
    d = [0 for _ in range(N + 1)]
    for u in range(1, N + 1):
        for v in range(1, N + 1):
            if all([pos[k][u] < pos[k][v] for k in range(1, K + 1)]):
                g[u].append(v)
                d[v] += 1

    # then find the longest path
    ans = 0
    for u in range(1, N + 1):
        if d[u] == 0:
            ans = max(ans, longestpath(u, g))
    return ans


def solve(N, K, A, pos):
    dp = [0 for _ in range(N + 1)]
    for i in range(1, N + 1):
        maxx = 0
        for p in range(1, i):
            # if the A[1][p], A[1][i] is the last two elements of ans
            # A[1][p] should appears before A[1][i] at every input array A[1:]
            if all([pos[k][A[1][p]] < pos[k][A[1][i]] for k in range(2, K + 1)]):
                maxx = max(maxx, dp[p])
        dp[i] = maxx + 1

    return max(dp)


N, K = map(int, input().split())
A = [[0] * (N + 1)]
pos = [[0 for _ in range(N + 1)] for _ in range(K + 1)]
for i in range(K):
    row = [0] + [int(x) for x in input().split()]
    A.append(row)
    for j, v in enumerate(row):
        pos[i + 1][v] = j

print(solve_graph(N, K, A, pos))
