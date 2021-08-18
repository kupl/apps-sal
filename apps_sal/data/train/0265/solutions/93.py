from collections import defaultdict


class Solution:
    def maxNonOverlapping(self, nums: List[int], target: int) -> int:

        dp = [0 for i in range(len(nums) + 1)]
        mp = {}
        s = 0
        mp[0] = 0
        for i in range(1, len(nums) + 1):
            s += nums[i - 1]
            dp[i] = dp[i - 1]
            if s - target in mp:
                dp[i] = max(dp[i], 1 + dp[mp[s - target]])
            if nums[i - 1] == target:
                dp[i] = max(dp[i], 1 + dp[i - 1])
            mp[s] = i
        return dp[-1]
