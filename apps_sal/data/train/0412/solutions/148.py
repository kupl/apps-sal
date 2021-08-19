class Solution:
    def numRollsToTarget(self, d: int, f: int, target: int) -> int:
        # dp
        dp = [[0 for i in range(target + 1)] for j in range(d + 1)]
        dp[0][0] = 1
        mod = 10**9 + 7
        for i in range(1, d + 1):
            for j in range(1, target + 1):
                for k in range(1, min(f, j) + 1):
                    dp[i][j] = (dp[i][j] + dp[i - 1][j - k]) % mod
        return dp[d][target] % mod
