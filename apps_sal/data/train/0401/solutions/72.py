class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        dp = [[0] * 3 for _ in range(len(nums) + 1)]
        dp[0][1] = float('-inf')
        dp[0][2] = float('-inf')

        for i in range(1, len(nums) + 1):
            if nums[i - 1] % 3 == 0:
                dp[i][0] = max(dp[i - 1][0], dp[i - 1][0] + nums[i - 1])
                dp[i][1] = max(dp[i - 1][1], dp[i - 1][1] + nums[i - 1])
                dp[i][2] = max(dp[i - 1][2], dp[i - 1][2] + nums[i - 1])
            elif nums[i - 1] % 3 == 1:
                dp[i][0] = max(dp[i - 1][0], dp[i - 1][2] + nums[i - 1])
                dp[i][1] = max(dp[i - 1][1], dp[i - 1][0] + nums[i - 1])
                dp[i][2] = max(dp[i - 1][2], dp[i - 1][1] + nums[i - 1])
            else:
                dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] + nums[i - 1])
                dp[i][1] = max(dp[i - 1][1], dp[i - 1][2] + nums[i - 1])
                dp[i][2] = max(dp[i - 1][2], dp[i - 1][0] + nums[i - 1])
        return dp[-1][0]
