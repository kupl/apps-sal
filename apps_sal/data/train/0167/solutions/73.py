
from math import inf
from typing import List


class Solution:

    def superEggDrop(self, K: int, N: int) -> int:
        self.memo = {}
        return self.rec(K, N)

    def rec(self, i, j):
        if i == 1:
            return j
        if j == 0 or j == 1:
            return j
        if (i, j) in self.memo:
            return self.memo[i, j]
        lo, hi = 0, j
        while lo < hi:
            mid = lo + (hi - lo) // 2
            left, right = self.rec(i - 1, mid - 1), self.rec(i, j - mid)
            if left < right:
                lo = mid + 1
            else:
                hi = mid
        res = 1 + self.max(self.rec(i - 1, lo - 1), self.rec(i, j - lo))
        self.memo[i, j] = res
        return res

    def dp(self, K: int, N: int) -> int:
        # dp[i][j] - i eggs for j floors
        dp = [[inf for _ in range(N + 1)] for _ in range(K + 1)]
        # dp[i][0] -> 0, dp[1][j] -> j, dp[i][1] -> 1
        for i in range(K + 1):
            dp[i][0] = 0
            dp[i][1] = 1
        for j in range(N + 1):
            dp[1][j] = j

        for i in range(2, K + 1):
            for j in range(2, N + 1):
                left, right = 0, j
                while left < right:
                    mid = left + (right - left) // 2
                    if dp[i - 1][mid - 1] < dp[i][j - mid]:
                        left = mid + 1
                    else:
                        right = mid
                dp[i][j] = 1 + self.max(dp[i - 1][left - 1], dp[i][j - left])
                # for k in range(i, j + 1):
                #    dp[i][j] = self.min(dp[i][j] , 1 + self.max(dp[i - 1][k - 1], dp[i][j - k])

        return dp[K][N]

    def min(self, a, b):
        return a if a < b else b

    def max(self, a, b):
        return a if a > b else b
