class Solution:

    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        m = len(str1)
        n = len(str2)
        dp = [[0 for x in range(n + 1)] for x in range(m + 1)]
        for i in range(m + 1):
            for j in range(n + 1):
                if i == 0 or j == 0:
                    dp[i][j] = 0
                elif str1[i - 1] == str2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        s = ''
        i = m
        j = n
        while i > 0 and j > 0:
            if str1[i - 1] == str2[j - 1]:
                s += str1[i - 1]
                i -= 1
                j -= 1
            elif dp[i - 1][j] > dp[i][j - 1]:
                i -= 1
            else:
                j -= 1
        res = s[::-1]
        (i, j, st) = (0, 0, 0)
        final = ''
        while i < m and j < n and (st < len(res)):
            if str1[i] != res[st]:
                final += str1[i]
                i += 1
            if str2[j] != res[st]:
                final += str2[j]
                j += 1
            elif str1[i] == res[st]:
                final += res[st]
                i += 1
                j += 1
                st += 1
        final += str2[j:] + str1[i:]
        return final
