class Solution:
    import functools

    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        longest = 0
        memo = {}

        def calc_lcs(i, j):
            if i < 0 or j < 0:
                return 0
            if (i, j) in memo:
                return memo[(i, j)]
            if text1[i] == text2[j]:
                return 1 + calc_lcs(i - 1, j - 1)
            memo[(i, j)] = max(calc_lcs(i, j - 1), calc_lcs(i - 1, j))
            return memo[(i, j)]
        return calc_lcs(len(text1) - 1, len(text2) - 1)
