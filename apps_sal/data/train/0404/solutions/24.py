class Solution:
    def largestSumOfAverages(self, A: List[int], K: int) -> float:
        n = len(A)
        dp = [[0]*(K+1) for _ in range(n+1)]
        
        for i in range(1, n+1):
            dp[i][1] = sum(A[:i])/i
        for i in range(2, n+1):
            for j in range(2, min(K+1, i+1)):
                dp[i][j] = max([dp[i-t][j-1] + sum(A[i-t:i]) / t for t in range(1,i)])
        return dp[n][K]
