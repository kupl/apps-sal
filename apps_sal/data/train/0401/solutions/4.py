class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [[0 for j in range(3)] for i in range(n)]
        dp[0][nums[0] % 3] = nums[0]
        for i in range(1, n):
            for j in range(3):
                dp[i][j] = dp[i - 1][j]
                if (j - nums[i]) % 3 == 0:
                    dp[i][j] = max(dp[i - 1][(j - nums[i]) % 3] + nums[i], dp[i - 1][j])
                else:
                    if dp[i - 1][(j - nums[i]) % 3] > 0:
                        dp[i][j] = max(dp[i - 1][(j - nums[i]) % 3] + nums[i], dp[i - 1][j])
        return dp[n - 1][0]
