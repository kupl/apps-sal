class Solution:

    def lastSubstring(self, s: str) -> str:
        i = 0
        j = i + 1
        k = 0
        while j + k < len(s):
            if s[i + k] == s[j + k]:
                k = k + 1
                continue
            elif s[i + k] > s[j + k]:
                j = j + 1
            else:
                i = max(i + k + 1, j)
                j = i + 1
            k = 0
        return s[i:]
