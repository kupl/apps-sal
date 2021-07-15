class Solution:
    def lastSubstring(self, s: str) -> str:
        maxchr = max(s)
        index = []
        maxstring = ''
        i = 0
        while i < len(s):
            if s[i] == maxchr:
                if i == 0 or s[i] != s[i-1]:
                    index.append(i)
                    maxstring = max(maxstring, s[i:])
            i += 1
        return maxstring
