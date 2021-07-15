class Solution:
    def largestSumOfAverages(self, A: List[int], K: int) -> float:
        prefix = [A[0]]
        for i in range(1, len(A)):
            prefix.append(prefix[i-1] + A[i])
            
        dp = [[prefix[i]/(i+1) if k == 1 else 0 for k in range(K+1)] for i in range(len(A))]
        
        for i in range(1, len(A)):
            for k in range(2, K+1):
                val = float('-inf')
                for j in range(1, i+1):
                    val = max(dp[j-1][k-1] + ((prefix[i] - prefix[j-1])/(i-j+1)), val)
                dp[i][k] = val
                
        return dp[len(A)-1][K]
