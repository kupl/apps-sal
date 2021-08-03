class Solution:
    def lcs_helper(self, s1, s2, lookup):
        m, n = len(s1), len(s2)
        lcs_look = lookup.get((m, n), -1)
        if m == 0 or n == 0:
            return 0
        if lcs_look != -1:
            return lcs_look
        if s1[-1] == s2[-1]:
            lcs_look = self.lcs_helper(s1[:-1], s2[:-1], lookup)
            lcs_look += 1
            lookup[(m, n)] = lcs_look
            return lcs_look
        else:
            lcs_look1 = self.lcs_helper(s1[:-1], s2, lookup)
            lcs_look2 = self.lcs_helper(s1, s2[:-1], lookup)
            lookup[(m, n)] = max(lcs_look1, lcs_look2)
            return lookup[(m, n)]

    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m, n = len(text1), len(text2)
        cache = {}
        if m == 0 or n == 0:
            return 0

        return self.lcs_helper(text1, text2, cache)
