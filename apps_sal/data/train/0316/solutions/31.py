class KMP:

    def Build(self, p):
        m = len(p)
        nxt = [0, 0]
        j = 0
        for i in range(1, m):
            while j > 0 and p[i] != p[j]:
                j = nxt[j]
            if p[i] == p[j]:
                j += 1
            nxt.append(j)
        return nxt

    def Match(self, s, p):
        n = len(s)
        m = len(p)
        nxt = self.Build(p)
        ans = []
        j = 0
        for i in range(n):
            while j > 0 and s[i] != p[j]:
                j = nxt[j]
            if s[i] == p[j]:
                j += 1
            if j == m:
                ans.append(i - m + 1)
                j = nxt[j]
        return ans


class Solution:

    def longestPrefix(self, s: str) -> str:
        kmp = KMP()
        nxt = kmp.Build(s)
        return s[:nxt[-1]]
