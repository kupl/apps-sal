class Solution:

    def maxNonOverlapping(self, nums: List[int], target: int) -> int:
        n = len(nums)
        dp = [0] * (n + 1)
        dic = {}
        dic[0] = 0
        curr = 0
        for i in range(1, n + 1):
            curr += nums[i - 1]
            if curr - target in dic:
                dp[i] = dp[dic[curr - target]] + 1
            dp[i] = max(dp[i - 1], dp[i])
            dic[curr] = i
        return dp[-1]
