class Solution:
    def numRollsToTarget(self, d: int, f: int, target: int) -> int:
        dp = [[0 for j in range(target + 1)] for i in range(d + 1)]
        for dd in range(1, d + 1):
            for tt in range(dd, min(dd * f, target) + 1):
                if dd == 1:
                    dp[dd][tt] = 1
                else:
                    for i in range(1, f + 1):
                        if tt - i >= 1:
                            dp[dd][tt] += dp[dd - 1][tt - i]
        return dp[dd][target] % (10**9 + 7)
