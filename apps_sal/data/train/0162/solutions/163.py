class Solution:

    def __init__(self):
        self.d = {}

    def longestCommonSubsequence(self, text1: str, text2: str) -> int:

        def lcs(p1, p2):
            if p1 == len(text1) or p2 == len(text2):
                return 0
            if (p1, p2) not in self.d:
                if text1[p1] == text2[p2]:
                    res = 1 + lcs(p1 + 1, p2 + 1)
                else:
                    res = max(lcs(p1 + 1, p2), lcs(p1, p2 + 1))
                self.d[p1, p2] = res
            return self.d[p1, p2]
        return lcs(0, 0)
