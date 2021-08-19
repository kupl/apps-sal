class Solution:

    def lastSubstring(self, s: str) -> str:
        i = 0
        j = i + 1
        k = 0
        while j + k < len(s):
            if s[i + k] > s[j + k]:
                j += 1
                k = 0
            elif s[i + k] < s[j + k]:
                i = j
                j = i + 1
                k = 0
            else:
                k += 1
        return s[i:]
