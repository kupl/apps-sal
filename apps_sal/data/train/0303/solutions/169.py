class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        n=len(arr)
        dp=[0]*(n+1)
        for i in range(n):
            m=-1
            x=-1
            for j in range(1,k+1):
                if (i-j+1)<0:
                    break
                x=max(x,arr[i-j+1])
                m=max(m,dp[i-j+1]+x*j)
            dp[i+1]=m
        return dp[n]
