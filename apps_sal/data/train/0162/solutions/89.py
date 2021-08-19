from functools import lru_cache


class Solution:

    def longestCommonSubsequence(self, txt1: str, txt2: str) -> int:

        @lru_cache(maxsize=None)
        def rec(i, j):
            if i == -1 or j == -1:
                return 0
            if txt1[i] == txt2[j]:
                return rec(i - 1, j - 1) + 1
            if txt1[i] != txt2[j]:
                return max(rec(i - 1, j), rec(i, j - 1))
        return rec(len(txt1) - 1, len(txt2) - 1)
