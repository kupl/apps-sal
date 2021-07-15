class Solution:
    def maxSumAfterPartitioning(self, A: List[int], K: int) -> int:
        N = len(A)
        dp = [0] * N
        dp[0] = A[0]

        for i in range(1, N):
            for j in range(0, min(K, i+1)):
                current_subarray = A[i-j:i+1]
                if i >= K:
                    dp[i] = max(dp[i], dp[i-j-1] + max(current_subarray)*(j+1))
                else:
                    dp[i] = max(dp[i], max(current_subarray)*(j+1))
            
        return dp[-1]
            
            
        # [1,15,7,9,2,5,10] k = 3
        # No need to inspect all combination, focus on growth
        
        # (1)
        # [1] -> 1 - max(A[i])*1
        
        # (1,15)
        # [1,15] -> 30 - max(A[i-1], A[i])*2
        # [1][15] -> 16 - DP[i-1] + A[i]
        
        0,1
        1,1
        
        # (1,15,7)
        # [1,15,7] -> 45 max(A[i]. A[i-1], A[-2])*3
        # [1][15,7] -> 23 - DP[i-2] + max(A[i-1], A[i])*2
        # [1,15][7] -> 37 - DP[i-1] + A[i]
        
        # (1,15,7,9)
        # [1,15,7][9] -> 54 DP[i-1] + A[i]
        # [1,15][7,9] -> 32 DP[i-2] + max(A[i-1], A[i])*2
        # [1][15,7,9] -> 46 DP[i-3] + max(A[i-2], A[i-1], A[i])*3
        

