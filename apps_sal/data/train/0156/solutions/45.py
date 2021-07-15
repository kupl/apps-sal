class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        
        
        @lru_cache(None)
        def lcs(x, y):
            
            m, n = len(x), len(y)
            
            dp = [['' for _ in range(n+1)] for _ in range(m+1)]
            
            for i in range(1, m+1):
                for j in range(1, n+1):
                    if x[i-1] == y[j-1]:
                        dp[i][j] = dp[i-1][j-1] + x[i-1]
                    else:
                        dp[i][j] = max(dp[i][j-1], dp[i-1][j], key=len)
                        
            return dp[-1][-1]

            
        # print(lcs(str1, str2))
        lcs_ = lcs(str1, str2)
        
        
        i = 0 
        j = 0
        res = ''
        for c in lcs_:
            while str1[i] != c:
                res += str1[i]
                i += 1
            while str2[j] != c:
                res += str2[j] 
                j += 1
                
            res += c
            i += 1
            j += 1
            
        # print(res)
        
        return res + str1[i:] + str2[j:]
            
            

