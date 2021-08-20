class Solution:

    def numRollsToTarget(self, d: int, f: int, target: int) -> int:
        dp: List[List[int]] = [[0] * (d + 1) for _ in range(target + 1)]
        for i in range(1, f + 1):
            if i <= target:
                dp[i][1] = 1
            else:
                break
        for j in range(2, d + 1):
            for i in range(j, target + 1):
                dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j] - dp[i - min(i - 1, f) - 1][j - 1]
        return dp[target][d] % (10 ** 9 + 7)
