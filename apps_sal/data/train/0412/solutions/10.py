class Solution:
    def numRollsToTarget(self, d, f, target):
        dp = [0] * (target + 1)
        dp[0] = 1
        for i in range(d):
            for j in range(target, -1, -1):
                tot = 0
                for k in range(1, 1 + min(f, j)):
                    tot += dp[j - k]
                dp[j] = tot
        return dp[target] % (10**9 + 7)
