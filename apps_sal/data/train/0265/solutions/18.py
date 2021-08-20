class Solution:

    def maxNonOverlapping(self, nums: List[int], target: int) -> int:
        dp = [0] + [-1] * len(nums)
        s = 0
        dic = {}
        dic[0] = 0
        res = 0
        for i in range(len(nums)):
            s += nums[i]
            if s - target in dic:
                dp[i + 1] = max(dp[dic[s - target]] + 1, dp[i])
            else:
                dp[i + 1] = dp[i]
            dic[s] = i + 1
        print(dp)
        return dp[-1]
