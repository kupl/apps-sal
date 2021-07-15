class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        def lcs(A, B):
            m, n = len(A), len(B)
            dp = [['' for _ in range(n + 1)] for _ in range(m + 1)]  
        
            for i in range(m):
                for j in range(n):        
                    if A[i] == B[j]:
                        dp[i + 1][j + 1] = dp[i][j] + A[i]
                    else:
                        dp[i + 1][j + 1] = max(dp[i + 1][j], dp[i][j + 1], key=len)
            
            return dp[-1][-1]
        
        ans = ''; i = j = 0
        for x in lcs(str1, str2):
            while str1[i] != x: ans += str1[i]; i += 1
            while str2[j] != x: ans += str2[j]; j += 1
            ans += x; i += 1; j += 1
        return ans + str1[i:] + str2[j:]
