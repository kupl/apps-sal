class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:

        lengthone = len(text1)
        lengthtwo = len(text2)

        n = 1000
        ans = [[0] * n for _ in range(n)]

        for i in range(lengthone):
            for j in range(lengthtwo):
                if text1[i] == text2[j]:
                    ans[i][j] = ans[i - 1][j - 1] + 1
                else:
                    ans[i][j] = max(ans[i - 1][j], ans[i][j - 1])

        return ans[lengthone - 1][lengthtwo - 1]
