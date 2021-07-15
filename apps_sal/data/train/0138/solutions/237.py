class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        dp = [[0]*2 for _ in range(len(nums))]
        dp[0][0] = nums[0] > 0
        dp[0][1] = nums[0] < 0
        ret = dp[0][0]
        for i in range(1,len(nums)):
            if nums[i] == 0:
                continue
            if nums[i] > 0:
                dp[i][0] = dp[i-1][0] + 1
                dp[i][1] = 0 if not dp[i-1][1] else dp[i-1][1] + 1
            else:
                dp[i][0] = 0 if not dp[i-1][1] else dp[i-1][1] + 1
                dp[i][1] = dp[i-1][0] + 1
            ret = max(ret,dp[i][0])
        return int(ret)
