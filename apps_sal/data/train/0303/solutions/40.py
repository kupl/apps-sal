class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        A=arr
        K=k
        n=len(A)
        dp=[0]*n
        for i in range(K):
            dp[i]=max(A[:i+1])*(i+1)
        for i in range(K,n):
            for j in range(1,K+1):
                dp[i]=max(dp[i],dp[i-j]+max(A[i-j+1:i+1])*j)
        return dp[-1]
        

