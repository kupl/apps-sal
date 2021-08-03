class Solution:
    def numRollsToTarget(self, d: int, f: int, target: int) -> int:
        mod = int(1e9) + 7

        dp = [[0 for _ in range(d + 1)] for _ in range(target + 1)]
        for i in range(1, min(target + 1, f + 1)):
            dp[i][1] = 1

        for i in range(2, target + 1):
            for j in range(2, d + 1):
                for k in range(1, min(f + 1, i + 1)):
                    dp[i][j] += dp[i - k][j - 1]

        return dp[target][d] % mod
