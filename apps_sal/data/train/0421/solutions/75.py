class Solution:  
    def lastSubstring(self, s: str) -> str:
        i, j, offset = 0, 1, 0
        while i + offset < len(s) and j + offset < len(s):
            if s[i + offset] == s[j + offset]:
                offset = offset + 1
            else:
                if s[i + offset] < s[j + offset]:
                    i = i + offset + 1
                    j = i + 1
                else:
                    j  = j + offset + 1
                offset = 0
        return s[i:]
