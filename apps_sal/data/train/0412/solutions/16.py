from functools import lru_cache


class Solution:
    @lru_cache
    def numRollsToTarget(self, d: int, f: int, target: int) -> int:

        dp = [[0] * (target + 1) for _ in range(d + 1)]
        dp[0][0] = 1
        for i in range(1, d + 1):
            for j in range(target + 1):
                if dp[i - 1][j] > 0:
                    for k in range(1, f + 1):
                        if j + k <= target:
                            dp[i][j + k] += dp[i - 1][j]
                            dp[i][j + k] %= (10**9 + 7)
        return dp[d][target]
