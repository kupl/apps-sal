from functools import lru_cache


class Solution:

    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        """
        base case:
        text1 = c1, text2 = c2
        if c1 == c2 return 1, if c1 != c2 return 0
        text1 = sub1 + c1 -> c1 is the last char
        text2 = sub2 + c2

        DP(text1, text2) = max(DP(text1, sub2), DP(sub1, text2), DP(sub1, sub2))
                           or DP(sub1, sub2) + 1 if c1 == c2
        """
        if len(text1) == 0 or len(text2) == 0:
            return 0

        @lru_cache(None)
        def lcs_of_sub(s1, s2):
            if not s1 or not s2:
                return 0
            (c1, c2) = (s1[-1], s2[-1])
            (sub1, sub2) = (s1[:-1], s2[:-1])
            if c1 == c2:
                return lcs_of_sub(sub1, sub2) + 1
            return max(lcs_of_sub(sub1, sub2), lcs_of_sub(sub1, s2), lcs_of_sub(s1, sub2))
        return lcs_of_sub(text1, text2)
