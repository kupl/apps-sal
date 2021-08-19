# ababdababc
# 0012012340

class Solution:
    def computelps(self, p: str):
        m = len(p)
        lps = [0] * m
        i = 1
        j = 0

        while i < m:
            if p[i] != p[j]:
                if j == 0:
                    i += 1
                else:
                    j = lps[j - 1]
            else:
                j += 1
                lps[i] = j
                i += 1
        return lps

    def longestPrefix(self, s: str) -> str:
        lps = self.computelps(s)

        return s[:lps[-1]]
