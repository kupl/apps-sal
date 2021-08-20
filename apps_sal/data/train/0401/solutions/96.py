class Solution:

    def maxSumDivThree(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [[0 for i in range(3)] for i in range(n + 1)]
        dp[0] = [0, -1e+18, -1e+18]
        for (i, v) in enumerate(nums):
            for k in range(3):
                dp[i + 1][k] = max(dp[i][k], v + dp[i][(k - v % 3 + 3) % 3])
        return dp[n][0]
