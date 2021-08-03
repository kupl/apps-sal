class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        dp = [[0, -1, -1] for _ in range(len(nums) + 1)]
        for i in range(1, len(nums) + 1):
            r = nums[i - 1] % 3
            for s in range(3):
                if dp[i - 1][s] >= 0:
                    dp[i][(r + s) % 3] = max(dp[i - 1][(r + s) % 3], dp[i - 1][s] + nums[i - 1])
                dp[i][s] = max(dp[i - 1][s], dp[i][s])

        return dp[len(nums)][0]
