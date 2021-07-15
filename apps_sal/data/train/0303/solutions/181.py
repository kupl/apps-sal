class Solution:
    def maxSumAfterPartitioning(self, A: List[int], K: int) -> int:
        dp = [0] * (len(A) + 1)
        
        for i in range(1, len(A) + 1):
            
            tmp = 0
            tmp_max = 0
            
            for j in range(1, min(i,K) + 1):
                tmp_max = max(A[i-j], tmp_max)
                tmp = max(tmp, dp[i-j] + tmp_max * j)
            
            dp[i] = tmp
        
        return dp[len(A)]
        

