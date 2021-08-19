class Solution:

    def numRollsToTarget(self, d, f, target, result=0):
        MOD = 7 + 1000000000.0
        dp = [0] * (1 + target)
        dp[0] = 1
        for i in range(1, 1 + d):
            newDP = [0] * (1 + target)
            prev = dp[0]
            for j in range(1, 1 + target):
                newDP[j] = prev
                prev = (prev + dp[j]) % MOD
                if j >= f:
                    prev = (prev - dp[j - f] + MOD) % MOD
            dp = newDP
        return int(dp[-1])
