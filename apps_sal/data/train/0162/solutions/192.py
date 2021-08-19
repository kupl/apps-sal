class Solution:

    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        record = [[0 for _ in range(len(text2))] for _ in range(len(text1))]

        def f(s1, s2, i, j):
            if i >= len(s1) or j >= len(s2):
                return 0
            if record[i][j] > 0:
                return record[i][j]
            if s1[i] == s2[j]:
                temp = 1 + f(s1, s2, i + 1, j + 1)
            else:
                temp = max(f(s1, s2, i, j + 1), f(s1, s2, i + 1, j))
            record[i][j] = temp
            return record[i][j]
        f(text1, text2, 0, 0)
        return record[0][0]
