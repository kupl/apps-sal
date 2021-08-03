from functools import lru_cache


class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        @lru_cache(maxsize=None)
        def rec(txt1, txt2, len1, len2):

            if len1 == 0 or len2 == 0:
                return 0
            if txt1[len1 - 1] == txt2[len2 - 1]:
                return rec(txt1, txt2, len1 - 1, len2 - 1) + 1
            else:
                return max(rec(txt1, txt2, len1 - 1, len2), rec(txt1, txt2, len1, len2 - 1))
        return rec(text1, text2, len(text1), len(text2))
