class Solution:

    def longestPrefix(self, s: str) -> str:
        long = 0
        for x in range(0, len(s) - 1):
            if s[0:x + 1] == s[len(s) - 1 - x:]:
                long = max(long, len(s[0:x + 1]))
        return s[:long]
