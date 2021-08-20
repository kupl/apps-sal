from functools import lru_cache


class Solution:

    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        (self.text1, self.text2) = (text1, text2)
        return self.lcs(0, 0)

    @lru_cache(maxsize=None)
    def lcs(self, from1, from2):
        if from1 >= len(self.text1) or from2 >= len(self.text2):
            return 0
        if self.text1[from1] == self.text2[from2]:
            return 1 + self.lcs(from1 + 1, from2 + 1)
        else:
            return max(self.lcs(from1, from2 + 1), self.lcs(from1 + 1, from2))
