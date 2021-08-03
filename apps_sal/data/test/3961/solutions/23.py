# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 1/8/20

"""

import collections
import time
import os
import sys
import bisect
import heapq
from typing import List


def solve(N, A):
    MOD = 10**9 + 7
    dp = [0 for _ in range(N + 1)]
    for i in range(N):
        dp[i + 1] = 2 * dp[i] + 2 - dp[A[i]]
        dp[i + 1] %= MOD
    return dp[N]


N = int(input())
A = [int(x) - 1 for x in input().split()]
print(solve(N, A))
