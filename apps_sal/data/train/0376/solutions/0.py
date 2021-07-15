class Solution:
    def minScoreTriangulation(self, A: List[int]) -> int:
        N = len(A)
        dp = [[0]*N for _ in range(N)]
        
        for i in range(N-2, -1, -1):
            for j in range(i+2, N):
                dp[i][j] = min(dp[i][k]+dp[k][j]+A[i]*A[j]*A[k] for k in range(i+1, j))
                
        return dp[0][-1]
                    
                

