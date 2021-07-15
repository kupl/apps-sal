class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        str1 = '0' + str1
        str2 = '0' + str2
        len_1, len_2 = len(str1), len(str2)
        
        dp = [[0] * len_2 for _ in range(len_1)]
        
        for i in range(1, len_1):
            for j in range(1, len_2):
                if str1[i] == str2[j]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        
        
        res = ''
        m, n = len_1 - 1, len_2 - 1
        while m > 0 or n > 0:
            if m == 0:
                res += str2[n]
                n -= 1
            elif n == 0:
                res += str1[m]
                m -= 1
            elif str1[m] == str2[n]:
                res += str1[m]
                m -= 1
                n -= 1
            elif dp[m-1][n] == dp[m][n]:
                res += str1[m]
                m -= 1
            elif dp[m][n-1] == dp[m][n]:
                res += str2[n]
                n -= 1
        # print(res)
        return res[::-1]

