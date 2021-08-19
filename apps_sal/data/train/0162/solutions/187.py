from functools import lru_cache


class Solution:

    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        self.text1 = text1
        self.text2 = text2
        return self.solve(len(text1), len(text2))

    @lru_cache(None)
    def solve(self, m, n):
        if not m or not n:
            return 0
        if self.text1[m - 1] == self.text2[n - 1]:
            return 1 + self.solve(m - 1, n - 1)
        else:
            return max(self.solve(m - 1, n), self.solve(m, n - 1))
