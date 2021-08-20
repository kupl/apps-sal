from functools import lru_cache


class Solution:

    def longestCommonSubsequence(self, text1: str, text2: str) -> int:

        @lru_cache(maxsize=None)
        def memo_solve(p1, p2):
            if len(text1) == p1 or len(text2) == p2:
                return 0
            if text1[p1] == text2[p2]:
                return 1 + memo_solve(p1 + 1, p2 + 1)
            else:
                return max(memo_solve(p1, p2 + 1), memo_solve(p1 + 1, p2))
        return memo_solve(0, 0)
