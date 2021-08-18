class Solution:
    def longestPrefix(self, s: str) -> str:
        for i in range(len(s) - 1, 0, -1):
            if s[:i] == s[len(s) - i:]:
                return s[:i]
        return ''
