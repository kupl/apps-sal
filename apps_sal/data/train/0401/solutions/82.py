class Solution:
    def maxSumDivThree(self, nums):
        N = len(nums)
        dp = [[0] * 3 for _ in range(2)]
        dp[0][nums[0] % 3] = nums[0]
        for n in range(1, N):
            row = n % 2
            alt = 1 - row
            r = nums[n] % 3
            for i in range(3):
                if dp[alt][i] > 0:
                    dp[row][(i + r) % 3] = dp[alt][i] + nums[n]
            for i in range(3):
                dp[row][i] = max(dp[row][i], dp[alt][i])
            dp[row][r] = max(dp[row][r], nums[n])
        return dp[1 - N % 2][0]
