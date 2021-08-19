class Solution:

    def maxNonOverlapping(self, nums: List[int], target: int) -> int:
        sm = 0
        hsh = {}
        dp = {}
        dp[-1] = 0
        ans = 0
        for i in range(len(nums)):
            dp[i] = dp[i - 1]
            sm += nums[i]
            if sm - target in hsh:
                dp[i] = max(dp[i], dp[hsh[sm - target]] + 1)
            hsh[sm] = i
            if sm == target:
                dp[i] = max(dp[i], 1)
            ans = max(ans, dp[i])
        return ans
