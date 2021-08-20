class Solution:

    def lastSubstring(self, s: str) -> str:
        i = 0
        j = 1
        k = 0
        while j + k < len(s):
            if s[i + k] == s[j + k]:
                k += 1
                continue
            elif s[i + k] > s[j + k]:
                j = j + k + 1
            else:
                i = j
                j = i + 1
            k = 0
        return s[i:]
