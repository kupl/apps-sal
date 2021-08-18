from functools import lru_cache


class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:

        @lru_cache(maxsize=None)
        def memo_solve(p1, p2):
            n = len(text1)
            m = len(text2)
            if n == p1 or m == p2:
                return 0

            if text1[p1] == text2[p2]:
                return 1 + memo_solve(p1 + 1, p2 + 1)

            return max(memo_solve(p1 + 1, p2), memo_solve(p1, p2 + 1))
        return memo_solve(0, 0)
