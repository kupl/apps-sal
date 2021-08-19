from functools import lru_cache as memoize


class Solution:

    def longestCommonSubsequence(self, text1, text2):

        @memoize(None)
        def lcs(s1, s2, m, n):
            if m == 0 or n == 0:
                return 0
            if s1[m - 1] == s2[n - 1]:
                return 1 + lcs(s1, s2, m - 1, n - 1)
            else:
                return max(lcs(s1, s2, m - 1, n), lcs(s1, s2, m, n - 1))
        return lcs(text1, text2, len(text1), len(text2))
