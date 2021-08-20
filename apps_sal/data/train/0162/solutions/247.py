class Solution:

    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        (n, m) = (len(text1), len(text2))
        arr = [[0] * (m + 1) for _ in range(n + 1)]
        for i in range(n + 1):
            for j in range(m + 1):
                if i == 0 or j == 0:
                    arr[i][j] = 0
                elif text1[i - 1] == text2[j - 1]:
                    arr[i][j] = 1 + arr[i - 1][j - 1]
                else:
                    arr[i][j] = max(arr[i - 1][j], arr[i][j - 1])
        return arr[-1][-1]
