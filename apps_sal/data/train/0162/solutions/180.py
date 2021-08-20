from functools import lru_cache


class Solution:

    def longestCommonSubsequence(self, text1: str, text2: str) -> int:

        @lru_cache(None)
        def helper(t1, t2):
            if not t1 or not t2:
                return 0
            if t1[-1] == t2[-1]:
                return helper(t1[:-1], t2[:-1]) + 1
            else:
                return max(helper(t1[:-1], t2), helper(t1, t2[:-1]))
        return helper(text1, text2)
