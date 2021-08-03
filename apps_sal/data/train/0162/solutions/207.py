class Solution:
    @lru_cache(maxsize=None)
    def longest(self, p1, p2):
        if p1 == len(self.t1) or p2 == len(self.t2):
            return 0

        if self.t1[p1] == self.t2[p2]:
            return 1 + self.longest(p1 + 1, p2 + 1)

        return max(self.longest(p1 + 1, p2), self.longest(p1, p2 + 1))

    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        self.t1 = text1
        self.t2 = text2
        return self.longest(0, 0)
