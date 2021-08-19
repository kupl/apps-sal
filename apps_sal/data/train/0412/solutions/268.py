class Solution:

    def numRollsToTarget(self, d: int, f: int, target: int) -> int:
        dp = [1] + [0] * target
        for i in range(d):
            for j in range(target, -1, -1):
                dp[j] = sum(dp[max(0, j - f):j])
        return dp[target] % (10 ** 9 + 7)
