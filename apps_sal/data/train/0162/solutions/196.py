from functools import lru_cache


class Solution:

    def longestCommonSubsequence(self, text1: str, text2: str) -> int:

        @lru_cache(maxsize=None)
        def recursion(text1: str, text2: str) -> int:
            if len(text1) == 0 or len(text2) == 0:
                return 0
            if text1[0] == text2[0]:
                return 1 + recursion(text1[1:], text2[1:])
            else:
                return max(recursion(text1, text2[1:]), recursion(text1[1:], text2))
        return recursion(text1, text2)
