class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [[0] * (3) for _ in range(n + 1)]
        dp[0] = [0, float('-inf'), float('-inf')]  # largest number with remainder 0,1,2
        for i in range(1, n + 1):
            x = nums[i - 1]
            if x % 3 == 0:
                for j in range(3):
                    dp[i][j] = dp[i - 1][j] + x
            elif x % 3 == 1:
                dp[i][0] = max(dp[i - 1][0], dp[i - 1][2] + x)
                dp[i][1] = max(dp[i - 1][1], dp[i - 1][0] + x)
                dp[i][2] = max(dp[i - 1][2], dp[i - 1][1] + x)
            elif x % 3 == 2:
                dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] + x)
                dp[i][1] = max(dp[i - 1][1], dp[i - 1][2] + x)
                dp[i][2] = max(dp[i - 1][2], dp[i - 1][0] + x)
        return dp[n][0]
