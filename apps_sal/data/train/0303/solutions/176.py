class Solution:
    def maxSumAfterPartitioning(self, A: List[int], K: int) -> int:
        N = len(A)
        dp = [0]*(N+1)
        
        for i in range(N):
            curr_max = 0
            for j in range(1, K+1):
                if i+j>N: break
                curr_max = max(curr_max, A[i+j-1])
                dp[i+j] = max(dp[i+j], dp[i]+curr_max*j)
                
        return dp[-1]
