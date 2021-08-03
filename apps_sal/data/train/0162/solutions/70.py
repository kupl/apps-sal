class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        '''
        f[i][j]: 前i个，前j个匹配的最长
        '''
        m, n = len(text1), len(text2)
        f = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(m + 1):
            for j in range(n + 1):
                if i == 0 and j == 0:
                    f[i][j] = 0
                elif i == 0:
                    f[i][j] = 0
                elif j == 0:
                    f[i][j] = 0
                else:
                    if text1[i - 1] == text2[j - 1]:
                        f[i][j] = max(f[i][j - 1], f[i - 1][j], f[i - 1][j - 1] + 1)
                    else:
                        f[i][j] = max(f[i][j - 1], f[i - 1][j])

        return f[m][n]
