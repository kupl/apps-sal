class Solution:

    def lastSubstring(self, s: str) -> str:
        if not s:
            return ''
        maxval = s
        maxstart = s[0]
        for i in range(len(s)):
            if s[i] >= maxstart and s[i:] > maxval:
                maxstart = s[i]
                maxval = s[i:]
        return maxval
