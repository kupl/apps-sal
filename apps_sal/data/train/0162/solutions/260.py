class Solution:
    def longestCommonSubsequence(self, A: str, B: str) -> int:
        if not A or not B:
            return 0
        
        m, n = len(A), len(B)
        f = [[None] * (n + 1) for _ in range(m + 1)]
        
        for i in range(m + 1):
            for j in range(n + 1):
                f[i][j] = 0
                if i == 0 or j == 0:
                    continue
                
                f[i][j] = max(f[i][j], f[i - 1][j], f[i][j - 1])
                
                if A[i - 1] == B[j - 1]:
                    f[i][j] = max(f[i][j], f[i - 1][j - 1] + 1)
        
        return f[m][n]

