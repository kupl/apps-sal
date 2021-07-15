class Solution:
    def largestSumOfAverages(self, A: List[int], K: int) -> float:
      
        n=len(A)
        dp=[[0]*(K+1) for _ in range(n)]
        s=0
        for i in range(n):
            s+=A[i]
            dp[i][1]=s*1.0/(i+1)
        
        for k in range(2,K+1):
            for i in range(k-1,n):
                s=0
                for m in range(i,k-2,-1):
                    s+=A[m]
                    dp[i][k]=max(dp[i][k],dp[m-1][k-1]+s*1.0/(i-m+1))
        return dp[-1][-1]
