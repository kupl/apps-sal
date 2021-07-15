class Solution:
    def constrainedSubsetSum(self, nums: List[int], k: int) -> int:
        n=len(nums)
        dp=[-sys.maxsize]*n
        dq=[]
        dp[n-1]=nums[n-1]
        res=dp[n-1]
        for i in range(n-2,-1,-1):
            while(len(dq)!=0 and dp[i+1]>dp[dq[-1]]):
                dq.pop()
            while(len(dq)!=0 and dq[0]>i+k):
                dq.pop(0)
            dq.append(i+1)
            dp[i]=max(dp[i],nums[i],nums[i]+dp[dq[0]])
            res=max(res,dp[i])
            
            
        return res

