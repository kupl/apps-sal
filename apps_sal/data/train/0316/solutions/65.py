class Solution:
    def longestPrefix(self, s: str) -> str:
        for i in range(len(s) - 1, -1, -1):
            if s[:i] == s[-i:]:
                return s[:i]
        return ''
