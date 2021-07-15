class Solution:
    def numRollsToTarget(self, d: int, f: int, target: int) -> int:
        MOD = 10 ** 9 + 7
        dp = [0] * (target + 1)
        dp[0] = 1
        for i in range(1, d + 1):
            for t in reversed(range(target + 1)):
                dp[t] = sum(dp[t - j] if t - j >= 0 else 0 for j in range(1, f + 1)) % MOD
        return dp[target]
