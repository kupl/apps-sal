class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        import numpy as np
        x = list(text1)
        y = list(text2)
        m = len(x)
        n = len(y)
        t = -1 * np.ones((m + 1, n + 1))
        for j in range(m + 1):
            t[j][0] = 0
        for i in range(n + 1):
            t[0][i] = 0
        print(t)
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if x[j - 1] == y[i - 1]:
                    t[j][i] = 1 + t[j - 1][i - 1]
                else:
                    t[j][i] = max(t[j - 1][i], t[j][i - 1])
        return int(t[m][n])
