class Solution:
    def longestPrefix(self, s: str) -> str:
        length = len(s)
        for i in range(1, length):
            if s[i] == s[0] and s[i:] == s[:length - i]:
                return s[i:]
        return ''
