class Solution:

    def numRollsToTarget(self, d: int, f: int, target: int) -> int:
        dp = [[0 for _ in range(target + 1)] for _ in range(d + 1)]
        for dd in range(1, d + 1):
            for tt in range(dd, min(f * dd, target) + 1):
                if dd == 1:
                    dp[dd][tt] = 1
                else:
                    dp[dd][tt] = sum(dp[dd - 1][max(1, tt - f):tt])
        return dp[d][target] % (10 ** 9 + 7)
