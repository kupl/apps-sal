class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        cache = {}

        def lcs(i, j):
            if i == len(text1) or j == len(text2):
                return 0
            if (i, j) in cache:
                return cache[(i, j)]
            if text1[i] == text2[j]:
                cache[(i, j)] = 1 + lcs(i + 1, j + 1)
                return cache[(i, j)]
            cache[(i, j)] = max(lcs(i + 1, j), lcs(i, j + 1))
            return cache[(i, j)]
        return lcs(0, 0)
