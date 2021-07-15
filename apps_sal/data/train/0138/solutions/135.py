class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        dp=[[0,0] for _ in range(len(nums))]
        if nums[0]>0:
            dp[0][0]=1
        elif nums[0]<0:
            dp[0][1]=1
        for i in range(1,len(nums)):
            if nums[i]==0:
                continue
            elif nums[i]>0:
                dp[i][0]=dp[i-1][0]+1
                if dp[i-1][1]>0:
                    dp[i][1]=dp[i-1][1]+1
            else:
                if dp[i-1][1]>0:
                    dp[i][0]=dp[i-1][1]+1
                dp[i][1]=dp[i-1][0]+1
        ans=0
        for i in dp:
            ans=max(ans,i[0])
        return ans

