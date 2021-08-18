class Solution:
    def longestSubarray(self, nums: List[int]) -> int:

        if not nums:
            return 0
        if all(nums):
            return len(nums) - 1

        n = len(nums)
        dp = [[0] * 2 for _ in range(n)]
        dp[0][0] = 1 if nums[0] == 1 else 0
        dp[0][1] = 0

        res = 0
        for i in range(1, n):
            if nums[i] == 1:
                dp[i][0] = dp[i - 1][0] + 1
                dp[i][1] = dp[i - 1][1] + 1
            else:
                dp[i][0] = 0
                dp[i][1] = dp[i - 1][0]

            res = max(res, dp[i][1], dp[i][0])
        return res
