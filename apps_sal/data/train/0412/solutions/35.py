class Solution:
    def numRollsToTarget(self, d, f, target):
        dp = [0] * (target+1)
        dp[0] = 1
        for i in range(d):
            for j in range(target, -1, -1):
                dp[j] = sum([dp[j-k] for k in range(1, 1+min(f, j))] or [0])
        return dp[target] % (10**9 + 7)
