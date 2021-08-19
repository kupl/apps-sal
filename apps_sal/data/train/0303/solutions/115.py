class Solution:

    def maxSumAfterPartitioning(self, nums: List[int], k: int) -> int:
        n = len(nums)
        dp = [nums[0]] + [0] * (n - 1)
        for i in range(1, n):
            for j in range(max(0, i - k + 1), i + 1):
                dp[i] = max(dp[i], dp[j - 1] + max(nums[j:i + 1]) * (i + 1 - j))
        return dp[-1]
