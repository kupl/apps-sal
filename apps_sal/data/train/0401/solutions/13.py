class Solution:

    def maxSumDivThree(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0
        dp = [[0] * 3 for i in range(n)]
        dp[0][nums[0] % 3] = nums[0]
        for i in range(1, n):
            t1 = nums[i] % 3
            dp[i][0] = max(dp[i - 1][(3 - t1) % 3] + nums[i], dp[i - 1][0]) if dp[i - 1][(3 - t1) % 3] != 0 else dp[i - 1][0]
            dp[i][1] = max(dp[i - 1][(3 - t1 + 1) % 3] + nums[i], dp[i - 1][1]) if dp[i - 1][(3 - t1 + 1) % 3] != 0 else dp[i - 1][1]
            dp[i][2] = max(dp[i - 1][(3 - t1 + 2) % 3] + nums[i], dp[i - 1][2]) if dp[i - 1][(3 - t1 + 2) % 3] != 0 else dp[i - 1][2]
            dp[i][t1] = max(nums[i], dp[i][t1])
        return dp[-1][0]
