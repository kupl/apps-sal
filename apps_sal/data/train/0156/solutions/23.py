class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        
        def lcs(text1, text2):
            m = len(text1)
            n = len(text2)
            dp = [['']*(n+1) for _ in range(m+1)]
            for i in range(1, m+1):
                for j in range(1, n+1):
                    if text1[i-1]==text2[j-1]:
                        dp[i][j] = dp[i-1][j-1] + text1[i-1]
                    else:
                        dp[i][j] = max(dp[i][j-1], dp[i-1][j], key=lambda x: len(x))
            return dp[-1][-1]
        
        if str1==str2:
            return str1
        i = 0
        j = 0
        ans = ''
        for c in lcs(str1, str2):
            while str1[i]!=c:
                ans += str1[i]
                i += 1
            while str2[j]!=c:
                ans += str2[j]
                j += 1
            ans += c
            i += 1
            j += 1
        return ans + str1[i:] + str2[j:]
