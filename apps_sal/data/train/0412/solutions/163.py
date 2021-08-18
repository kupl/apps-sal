class Solution:
    def numRollsToTarget(self, d: int, f: int, target: int) -> int:
        dp = [[0 for _ in range(target + 1)] for _ in range(d + 1)]
        for i in range(1, min(f + 1, target + 1)):
            dp[1][i] = 1
        for i in range(1, d + 1):
            for j in range(2, target + 1):
                for k in range(1, f + 1):
                    if j - k >= 0:
                        dp[i][j] += dp[i - 1][j - k]
        return dp[-1][-1] % 1000000007
