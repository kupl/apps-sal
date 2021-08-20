class Solution:

    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        m = len(str1)
        n = len(str2)
        DP = [[0 for j in range(n + 1)] for i in range(m + 1)]
        res = []
        for i in range(m + 1):
            DP[i][0] = i
        for j in range(n + 1):
            DP[0][j] = j
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if str1[i - 1] == str2[j - 1]:
                    DP[i][j] = 1 + DP[i - 1][j - 1]
                elif DP[i - 1][j] < DP[i][j - 1]:
                    DP[i][j] = 1 + DP[i - 1][j]
                else:
                    DP[i][j] = 1 + DP[i][j - 1]
        i = m
        j = n
        res = []
        while i > 0 or j > 0:
            if i - 1 >= 0 and j - 1 >= 0 and (str1[i - 1] == str2[j - 1]):
                res.append(str1[i - 1])
                i -= 1
                j -= 1
            elif DP[i - 1][j] < DP[i][j - 1]:
                res.append(str1[i - 1])
                i -= 1
            else:
                res.append(str2[j - 1])
                j -= 1
        return ''.join(reversed(res))
