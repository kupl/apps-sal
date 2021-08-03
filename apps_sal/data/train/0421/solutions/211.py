class Solution:
    def lastSubstring(self, s: str) -> str:
        max = 0
        i = 1
        j = 0
        while i + j < len(s):
            if s[i + j] == s[max + j]:
                j = j + 1
            elif s[i + j] > s[max + j]:
                max = i
                j = 0
                i = i + 1
            else:
                j = 0
                i = i + 1

        return s[max:]
