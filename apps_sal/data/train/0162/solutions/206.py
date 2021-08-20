class Solution:

    def __init__(self):
        self.cached = {}

    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        if len(text1) == 0 or len(text2) == 0:
            return 0
        if (len(text1), len(text2)) in self.cached:
            return self.cached[len(text1), len(text2)]
        if text1[-1] == text2[-1]:
            r = self.longestCommonSubsequence(text1[:-1], text2[:-1]) + 1
        else:
            r = max(self.longestCommonSubsequence(text1, text2[:-1]), self.longestCommonSubsequence(text1[:-1], text2))
        self.cached[len(text1), len(text2)] = r
        return r
