class Solution:
    def maxUncrossedLines(self, A: List[int], B: List[int]) -> int:
        m, n = len(A), len(B)
        dp = [[0] * n for _ in range(m)]
        
        # dp[0][0] = int(A[0] == B[0])
        
        for i in range(m):
            for j in range(n):
                left = dp[i][j-1] if j>0 else 0
                up = dp[i-1][j] if i>0 else 0
                leftup = dp[i-1][j-1] if i>0 and j>0 else 0
                dp[i][j] = max(left, up, leftup + int(A[i]==B[j]))
                print(left, up, leftup)
        
        return dp[m-1][n-1]
