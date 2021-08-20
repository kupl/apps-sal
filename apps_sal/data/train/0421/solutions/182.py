class Solution:

    def lastSubstring(self, s: str) -> str:
        (i, j) = (0, 1)
        k = 0
        while j + k < len(s):
            if s[i + k] == s[j + k]:
                k += 1
            elif s[i + k] > s[j + k]:
                j += k + 1
                k = 0
            else:
                i = j
                j = i + 1
                k = 0
        return s[i:]
