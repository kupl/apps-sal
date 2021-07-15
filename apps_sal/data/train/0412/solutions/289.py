class Solution:
    def numRollsToTarget(self, d: int, f: int, target: int) -> int:
        if target < d or target > d * f:
            return 0
        dp = [0] * (target + 1)
        dp[0] = 1
        mod_val = 10 ** 9 + 7
        for r in range(1, d + 1):
            if r > 1:
                dp[r - 2] = 0
            for i in range(target, r - 1, -1):
                dp[i] = sum(dp[max(0, i - f) : i]) % mod_val
        return dp[target]
