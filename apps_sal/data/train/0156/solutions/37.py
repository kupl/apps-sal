class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        n = len(str1)
        m = len(str2)
        
        dp = [[-1] * (m + 1) for _ in range(n + 1)]
        
        for i in range(n + 1):
            for j in range(m + 1):
                if i == 0 or j == 0:
                    dp[i][j] = 0
                else:
                    if str1[i - 1] == str2[j - 1]:
                        dp[i][j] = 1 + dp[i - 1][j - 1]
                    else:
                        dp[i][j] = max(dp[i][j - 1], dp[i - 1][j])
        
        i = n
        j = m
        result = []
        while i > 0 and j > 0:
            if str1[i - 1] == str2[j - 1]:
                result.append(str1[i - 1])
                i -= 1
                j -= 1
            else:
                left = dp[i][j - 1]
                top = dp[i - 1][j]
                if left > top:
                    result.append(str2[j - 1])
                    j -= 1
                else:
                    result.append(str1[i - 1])
                    i -= 1
        
        while i > 0:
            result.append(str1[i - 1])
            i -= 1
        while j > 0:
            result.append(str2[j - 1])
            j -= 1
        
        result = ''.join(result[::-1])
        return result
                

