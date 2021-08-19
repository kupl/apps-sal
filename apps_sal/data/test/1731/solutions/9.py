# -*- coding: utf-8 -*-

import math
import collections
import bisect
import heapq
import time
import random
import itertools
import sys
from typing import List

"""
created by shhuan at 2020/1/14 22:56

"""


def solve(N, M):
    MOD = 10 ** 9 + 7
    dp = [[0 for _ in range(N + 1)] for _ in range(1 + M)]
    for v in range(1, N + 1):
        dp[1][v] = 1
    for i in range(2, M + 1):
        for v in range(1, N + 1):
            dp[i][v] = sum([dp[i - 1][u] for u in range(1, v + 1)])
            dp[i][v] %= MOD

    dp2 = [[0 for _ in range(N + 1)] for _ in range(1 + M)]
    for v in range(1, N + 1):
        dp2[1][v] = 1
    for i in range(2, M + 1):
        for v in range(1, N + 1):
            dp2[i][v] = sum([dp2[i - 1][u] for u in range(v, N + 1)])
            dp2[i][v] %= MOD

    ans = 0
    for v in range(1, N + 1):
        ans += sum([dp[M][v] * dp2[M][u] for u in range(v, N + 1)])
        ans %= MOD

    return ans


N, M = map(int, input().split())
print(solve(N, M))
