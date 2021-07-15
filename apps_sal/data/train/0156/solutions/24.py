class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        n1, n2 = len(str1), len(str2)
        dp = [[0 for j in range(n2+1)] for i in range(n1+1)]
        for i in range(1, n1+1):
            for j in range(1, n2+1):
                if str1[i-1] == str2[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        i, j, ans = n1-1, n2-1, ''
        while i >= 0 and j >= 0:
            if dp[i+1][j+1] == dp[i][j+1]:
                ans = str1[i] + ans
                i -= 1
            elif dp[i+1][j+1] == dp[i+1][j]:
                ans = str2[j] + ans
                j -= 1
            else:
                ans = str1[i] + ans
                i -= 1
                j -= 1
        if i < 0:
            ans = str2[:j+1] + ans
        else:
            ans = str1[:i+1] + ans
        return ans
            
            
        

