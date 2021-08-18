class Solution:
    @lru_cache(None)
    def numRollsToTarget(self, d: int, f: int, target: int) -> int:
        dp = [1] + [0] * target
        mod = 10**9 + 7
        for _ in range(d):
            for i in range(target, -1, -1):
                dp[i] = sum(dp[i - ff] for ff in range(1, f + 1) if i >= ff) % mod
        return dp[-1] % mod

        dp = [[0] * (target + 1) for _ in range(d + 1)]
        mod = 10 ** 9 + 7
        dp[0][0] = 1
        for i in range(1, d + 1):
            for j in range(1, target + 1):
                dp[i][j] = (sum(dp[i - 1][j - ff] for ff in range(1, f + 1) if j >= ff))
        return dp[-1][-1] % mod
