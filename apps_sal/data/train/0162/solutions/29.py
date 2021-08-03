from functools import lru_cache


class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:

        @lru_cache(maxsize=None)
        def memo(l1, l2):
            if l1 == len(text1) or l2 == len(text2):
                return 0
            if text1[l1] == text2[l2]:
                return 1 + memo(l1 + 1, l2 + 1)
            else:
                return max(memo(l1 + 1, l2), memo(l1, l2 + 1))
        return memo(0, 0)
