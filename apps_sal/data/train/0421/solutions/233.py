class Solution:

    def lastSubstring(self, s: str) -> str:
        (i, j, off) = (0, 1, 0)
        while i + off < len(s) and j + off < len(s):
            if s[i + off] == s[j + off]:
                off += 1
            else:
                if s[i + off] > s[j + off]:
                    j += 1
                else:
                    i = j
                    j = j + 1
                off = 0
        return s[i:]
