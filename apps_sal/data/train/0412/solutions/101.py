class Solution:
    def numRollsToTarget(self, d: int, f: int, target: int) -> int:
        dp = [[0] * (d + 1) for _ in range(target + 1)]
        dp[0][0] = 1
        for i in range(1, target + 1):
            for j in range(1, d + 1):
                if i >= j:
                    for num in range(1, min(i, f) + 1):
                        dp[i][j] += dp[i - num][j - 1]
        return dp[-1][-1] % (10 ** 9 + 7)
