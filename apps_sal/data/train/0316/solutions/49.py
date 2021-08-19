class Solution:

    def longestPrefix(self, s: str) -> str:
        t = [-1]
        (pos, cnd) = (1, 0)
        while pos < len(s) - 1:
            if s[pos] == s[cnd]:
                t.append(t[cnd])
            else:
                t.append(cnd)
                cnd = t[cnd]
                while cnd >= 0 and s[pos] != s[cnd]:
                    cnd = t[cnd]
            pos += 1
            cnd += 1
        t.append(cnd)
        (j, k) = (1, 0)
        while j < len(s):
            if s[k] == s[j]:
                j += 1
                k += 1
                if k == len(s):
                    k = t[k]
            else:
                k = t[k]
                if k < 0:
                    j += 1
                    k += 1
        return s[:k]
