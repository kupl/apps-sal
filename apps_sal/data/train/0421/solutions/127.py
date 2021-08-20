class Solution:

    def lastSubstring(self, s: str) -> str:
        (m, i, k) = (0, 1, 0)
        while i + k < len(s):
            if s[m + k] == s[i + k]:
                k += 1
            elif s[m + k] > s[i + k]:
                i = i + k + 1
                k = 0
            else:
                m = max(m + k + 1, i)
                i = m + 1
                k = 0
        return s[m:]
