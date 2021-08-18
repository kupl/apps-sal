class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:

        cache = [[-1 for _ in range(len(text2))] for _ in range(len(text1))]

        def lcs(text1, text2, i, j, cache):

            if i >= len(text1) or j >= len(text2):
                return 0
            if cache[i][j] != -1:
                return cache[i][j]
            elif text1[i] == text2[j]:
                return 1 + lcs(text1, text2, i + 1, j + 1, cache)
            else:
                cache[i][j] = max(lcs(text1, text2, i, j + 1, cache), lcs(text1, text2, i + 1, j, cache))
                return cache[i][j]

        a = lcs(text1, text2, 0, 0, cache)

        return a
