class Solution:
    def numRollsToTarget(self, d: int, f: int, target: int) -> int:
        dp = [0] * (target + 1)
        dp[0] = 1
        for i in range(d):
            dp_new = [0] * len(dp)
            for i in range(1, len(dp)):
                for j in range(1, f + 1):
                    if i - j >= 0:
                        dp_new[i] = (dp_new[i] + dp[i - j]) % (10**9 + 7)
            dp = dp_new
        return dp[-1] % (10**9 + 7)
