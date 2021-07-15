class Solution:
    def maxSumAfterPartitioning(self, A: List[int], K: int) -> int:
        n = len(A)
        dp = [0] * n
        
        for i in range(K):
            dp[i] = max(A[:i+1]) * (i + 1)
        
        for i in range(K, n):
            for d in range(1, K + 1):
                dp[i] = max(dp[i], dp[i - d] + max(A[i - d + 1: i + 1]) * d)
                
        return dp[-1]
