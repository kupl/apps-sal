from typing import List
import collections
import heapq
import itertools
import bisect
import copy
import random
import re
import fractions
import math

mod = 10 ** 9 + 7


class Solution:
    def dieSimulator(self, n: int, rollMax: List[int]) -> int:

        rollMax = [0] + rollMax
        dp = [[[0] * 17 for _ in range(7)] for _2 in range(n)]
        dp[0] = [[0, 1] + [0] * 15 for _ in range(7)]

        for m in range(1, n):
            for i in range(1, 7):
                for j in range(1, 7):
                    for k in range(1, rollMax[j] + 1):
                        if i == j:
                            if k < rollMax[i]:
                                dp[m][i][k + 1] += dp[m - 1][i][k] % mod
                        else:
                            dp[m][i][1] += dp[m - 1][j][k] % mod

        return sum(map(sum, dp[n - 1])) % mod
