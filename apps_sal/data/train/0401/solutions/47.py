class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        dp=[0,0,0]
        for num in nums:
            newlist=dp.copy()
            for i in range(len(dp)):
                curr=newlist[i]+num
                dp[curr%3]=max(dp[curr%3],curr)
        return dp[0]
