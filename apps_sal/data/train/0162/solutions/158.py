class Solution:

    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        t = [[-1 for j in range(len(text2) + 1)] for i in range(len(text1) + 1)]
        for i in range(len(text1) + 1):
            for j in range(len(text2) + 1):
                t[0][j] = 0
                t[i][0] = 0
        res = self.LCS(text1, text2, len(text1), len(text2), t)
        return res

    def LCS(self, s1, s2, n, m, t):
        if t[n][m] != -1:
            return t[n][m]
        elif s1[n - 1] == s2[m - 1]:
            t[n][m] = self.LCS(s1, s2, n - 1, m - 1, t) + 1
            return t[n][m]
        elif s1[n - 1] != s2[m - 1]:
            t[n][m] = max(self.LCS(s1, s2, n - 1, m, t), self.LCS(s1, s2, n, m - 1, t))
            return t[n][m]
