class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        m, n = len(str1), len(str2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for x in range(1, m + 1):
            for y in range(1, n + 1):
                if str1[x - 1] == str2[y - 1]:
                    dp[x][y] = 1 + dp[x - 1][y - 1]
                else:
                    dp[x][y] = max(dp[x - 1][y], dp[x][y - 1])
        i, j = m, n
        res = ''
        while(i > 0 and j > 0):
            if(str1[i - 1] == str2[j - 1]):
                res = str1[i - 1] + res
                i -= 1
                j -= 1
            elif(dp[i - 1][j] == dp[i][j]):
                res = str1[i - 1] + res
                i -= 1
            else:
                res = str2[j - 1] + res
                j -= 1
        while(i > 0):
            res = str1[i - 1] + res
            i -= 1
        while(j > 0):
            res = str2[j - 1] + res
            j -= 1
        return res
