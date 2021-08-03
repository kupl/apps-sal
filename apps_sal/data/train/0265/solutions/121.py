class Solution:
    def maxNonOverlapping(self, nums: List[int], target: int) -> int:
        seen = {0: -1}
        dp = [0] * (len(nums))
        ans = 0
        for i in range(len(nums)):
            if(i > 0):
                nums[i] += nums[i - 1]
                dp[i] = dp[i - 1]
            if((nums[i] - target) in seen):
                dp[i] = max(dp[i], dp[seen[nums[i] - target]] + 1)
            seen[nums[i]] = i
        return dp[-1]
