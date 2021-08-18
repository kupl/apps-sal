class Solution:
    def numRollsToTarget(self, d: int, f: int, target: int) -> int:
        MOD = (10 ** 9) + 7

        f = min(f, target)

        dp = [[0 for t in range(target + 1)] for r in range(d)]

        for i in range(1, f + 1):
            dp[0][i] = 1

        for r in range(1, d):
            for i in range(1, target + 1):
                for val in range(1, f + 1):
                    if i - val >= 0:
                        dp[r][i] = (dp[r - 1][i - val] + dp[r][i]) % MOD

        return dp[-1][target]
