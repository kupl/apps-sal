class Solution:
    def maxUncrossedLines(self, A: List[int], B: List[int]) -> int:
        
        m = len(A)
        n = len(B)
        dp = [[0 for j in range(n+1)] for i in range(m+1)]
        for i in range(m+1):
            for j in range(n+1):
                if(i==0 or j==0):
                    dp[i][j] = 0
                elif(A[i-1]==B[j-1]):
                    dp[i][j] = 1 + dp[i-1][j-1]
                else:
                    dp[i][j] = max(dp[i-1][j],dp[i][j-1])
        
        print(dp)
        return dp[m][n]
