class Solution:

    def numRollsToTarget(self, d: int, f: int, target: int) -> int:
        if not d or not f or (not target):
            return 0
        dp = [[0] * (target + 1) for _ in range(d + 1)]
        dp[0][0] = 1
        for i in range(1, len(dp)):
            for j in range(1, len(dp[0])):
                k = 1
                while k <= min(j, f):
                    dp[i][j] += dp[i - 1][j - k]
                    k += 1
        return dp[-1][-1] % (10 ** 9 + 7)
