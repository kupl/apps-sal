class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:

        d = [[None] * (len(text2) + 1) for _ in range(len(text1) + 1)]
        for j in range(len(text2) + 1):
            d[0][j] = 0
        for i in range(len(text1) + 1):
            d[i][0] = 0
        i = 1
        while i < len(text1) + 1:
            j = 1
            while j < len(text2) + 1:
                if text1[i - 1] == text2[j - 1]:
                    d[i][j] = max(d[i - 1][j - 1] + 1, d[i][j - 1], d[i - 1][j])
                else:
                    d[i][j] = max(d[i][j - 1], d[i - 1][j])
                j += 1
            i += 1
        return max([max(row) for row in d])
