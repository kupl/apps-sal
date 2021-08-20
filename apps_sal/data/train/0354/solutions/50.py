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
        dp = [[0, 1] + [0] * 15 for _ in range(7)]
        for _ in range(2, n + 1):
            dp2 = [[0] * 17 for _ in range(7)]
            for i in range(1, 7):
                for j in range(1, 7):
                    for k in range(1, rollMax[j] + 1):
                        if i == j:
                            if k < rollMax[i]:
                                dp2[i][k + 1] += dp[i][k] % mod
                        else:
                            dp2[i][1] += dp[j][k] % mod
            dp = dp2
        return sum(map(sum, dp)) % mod
