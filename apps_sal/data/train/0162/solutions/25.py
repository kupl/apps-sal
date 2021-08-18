from collections import defaultdict


class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:

        @lru_cache(maxsize=None)
        def helper(n, m):
            if m < 0 or n < 0:
                return 0
            if text1[n] == text2[m]:
                length = 1 + helper(n - 1, m - 1)
            else:
                length = max(helper(n - 1, m),
                             helper(n, m - 1))
            return length
        return helper(len(text1) - 1, len(text2) - 1)
