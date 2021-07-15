class Solution:
    def longestCommonSubsequence(self, s1: str, s2: str) -> int:
        def rec(s1, s2, i, j, lcs):
            if i == len(s1) or j == len(s2):
                return 0
            if (i, j) in lcs:
                return lcs[(i, j)]
            else:
                if s1[i] == s2[j]:
                    lcs[(i, j)] = 1 + rec(s1, s2, i + 1, j + 1, lcs)
                else:
                    l = rec(s1, s2, i + 1, j, lcs)
                    r = rec(s1, s2, i, j + 1, lcs)
                    lcs[(i, j)] = max(l, r)
                return lcs[(i, j)]
        return rec(s1, s2, 0, 0, {})
