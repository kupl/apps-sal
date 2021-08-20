class Solution:

    def numRollsToTarget(self, d: int, f: int, target: int) -> int:
        if target > d * f:
            return 0
        if target == d * f:
            return 1
        if d == 1:
            return 1
        if f > target:
            f = target
        MOD = 10 ** 9 + 7
        dp = [[0 for j in range(d * f + 1 + 1)] for i in range(d + 1)]
        for i in range(1, f + 1):
            dp[1][i] = 1
        for i in range(d + 1):
            for j in range(d * f + 1 + 1):
                for t in range(1, f + 1):
                    if j - t >= i - 1:
                        dp[i][j] += dp[i - 1][j - t] % MOD
        return dp[d][target] % MOD
