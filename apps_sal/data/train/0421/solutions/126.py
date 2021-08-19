class Solution:

    def lastSubstring(self, s: str) -> str:
        maxChar = s[0]
        for c in s:
            maxChar = max(maxChar, c)
        print(maxChar)
        check = ''
        for i in range(0, len(s)):
            if s[i] == maxChar and s[i:] > check:
                check = s[i:]
        return check
