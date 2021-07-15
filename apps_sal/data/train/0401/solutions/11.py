class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:        
        dp=[[0]*3 for i in range(len(nums))]
        for i in range(len(dp)):
            dp[i]=list(dp[i-1])
            for k in range(3):
                index=((dp[i-1][k] if i-1>=0 else 0)+nums[i])%3
                dp[i][index]=max((dp[i-1][k] if i-1>=0 else 0)+nums[i],dp[i][index])
        return dp[-1][0]
