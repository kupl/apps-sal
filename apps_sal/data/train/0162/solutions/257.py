class Solution:
    def longestCommonSubsequence(self, a: str, b: str) -> int:
        m, n = len(a), len(b)
        c = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
        for i in range(m + 1):
            for j in range(n + 1):
                if i == 0 or j == 0: c[i][j] = 0
                else:
                    if a[i - 1] == b[j - 1]: c[i][j] = max([c[i - 1][j], c[i][j - 1], c[i - 1][j - 1] + 1])
                    else: c[i][j] = max([c[i - 1][j], c[i][j - 1]])
        return c[m][n]

