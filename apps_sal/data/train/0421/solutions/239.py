class Solution:
    def lastSubstring(self, s: str) -> str:
        i = 0
        k = 0
        j = 1
        while j + k < len(s):
            if s[i + k] == s[j + k]:
                k += 1
                continue
            elif s[i + k] > s[j + k]:
                j += 1
            else:
                i += 1

            if i == j:
                j += 1
            k = 0
        return s[i:]
