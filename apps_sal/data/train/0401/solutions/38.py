class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0,float('-inf'),float('-inf')] # largest number with remainder 0,1,2
        for i in range(1,n+1):
            x = nums[i-1]
            dp1 = [0]*3
            if x%3==0:
                for j in range(3):
                    dp1[j] = dp[j]+x
            elif x%3==1:
                dp1[0] = max(dp[0],dp[2]+x)
                dp1[1] = max(dp[1],dp[0]+x)
                dp1[2] = max(dp[2],dp[1]+x)
            elif x%3==2:
                dp1[0] = max(dp[0],dp[1]+x)
                dp1[1] = max(dp[1],dp[2]+x)
                dp1[2] = max(dp[2],dp[0]+x)
            dp=dp1
        return dp[0]

