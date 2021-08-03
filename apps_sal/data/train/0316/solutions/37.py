class Solution:
    def longestPrefix(self, s: str) -> str:
        def build(p):
            m = len(p)
            nxt = [0, 0]
            j = 0
            for i in range(1, m):
                while j > 0 and s[i] != s[j]:
                    j = nxt[j]
                if s[i] == s[j]:
                    j += 1
                nxt.append(j)
            return nxt

        nxt = build(s)
        return s[:nxt[-1]]
