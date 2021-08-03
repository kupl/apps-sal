class Solution:
    def numRollsToTarget(self, d: int, f: int, target: int) -> int:
        dp = [[0 for j in range(target + 1)] for i in range(d)]
        for j in range(1, min(f, target) + 1):
            dp[0][j] = 1
        for i in range(1, d):
            for j in range(1, target + 1):
                for k in range(1, f + 1):
                    if j < k:
                        break
                    dp[i][j] += dp[i - 1][j - k]
        return dp[d - 1][target] % (10**9 + 7)
