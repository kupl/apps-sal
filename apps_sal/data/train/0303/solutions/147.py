class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        
        A = arr
        
        K = k
        
        n = len(A)
        dp = [0] * n
        curMax = 0
        for i in range(n):
            if i < K: 
                curMax = max(curMax, A[i])
                dp[i] = curMax * (i + 1)
            else:
                curMax = 0
                for j in range(1, K + 1):
                    curMax = max(A[i - j + 1], curMax)
                    dp[i] = max(dp[i], dp[i - j] + curMax * j)
                    
                    
        # print(dp)
        
        return dp[n - 1]
