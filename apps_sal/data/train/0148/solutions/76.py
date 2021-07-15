class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        n=len(profit)
        maxm=max(difficulty)
        dp=[0]*(1+maxm)
        for i in range(n):
            dp[difficulty[i]]=max(dp[difficulty[i]],profit[i])
        for i in range(1,maxm+1):
            dp[i]=max(dp[i],dp[i-1])
        res=0

        for x in worker:
            if x>maxm:
                res+=dp[maxm]
            else:
                res+=dp[x]
        return res
