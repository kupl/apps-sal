class Solution:

    def lastSubstring(self, s: str) -> str:
        lastSubstring = s
        for i in range(1, len(s)):
            if s[i:] > lastSubstring:
                lastSubstring = s[i:]
        return lastSubstring
