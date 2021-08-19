class Solution:

    def longestPrefix(self, s: str) -> str:
        p1 = s[0]
        length = len(s)
        for i in range(1, len(s)):
            if s[i] == p1:
                if s[i:] == s[:length - i]:
                    return s[i:]
        return ''
