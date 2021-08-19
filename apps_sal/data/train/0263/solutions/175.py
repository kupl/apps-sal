import numpy as np


class Solution:

    def knightDialer(self, n: int) -> int:
        (memo, dp) = ([[4, 6], [8, 6], [7, 9], [4, 8], [3, 9, 0], [], [0, 1, 7], [2, 6], [1, 3], [2, 4]], [1] * 10)
        for i in range(n - 1):
            dp = [sum([dp[j] for j in memo[i]]) for i in range(10)]
        return sum(dp) % (10 ** 9 + 7)
