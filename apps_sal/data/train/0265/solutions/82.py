class Solution:
    def maxNonOverlapping(self, nums: List[int], target: int) -> int:
        n = len(nums)
        dp = [0 for i in range(n+1)]
        d = {}
        d[0] = -1
        s = 0
        for i in range(n):
            s+=nums[i]
            t = s-target
            dp[i+1] = dp[i]
            if t in d:
                dp[i+1] = max(dp[i+1],dp[d[t]+1]+1)
            d[s] = i
        # print(d)
        return dp[n]
