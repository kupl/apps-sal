class Solution:

    def maxSumDivThree(self, nums: List[int]) -> int:
        dp = [[0] * 3 for _ in range(len(nums) + 1)]
        for (i, n) in enumerate(nums):
            r = n % 3
            for j in range(3):
                if dp[i][j] > 0:
                    dp[i + 1][(j + r) % 3] = max(dp[i][j] + n, dp[i][(j + r) % 3])
                else:
                    dp[i + 1][(j + r) % 3] = dp[i][(j + r) % 3]
            dp[i + 1][r] = max(n, dp[i + 1][r])
        return dp[-1][0]
