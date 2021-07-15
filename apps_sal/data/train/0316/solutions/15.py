class Solution:
    def longestPrefix(self, s: str) -> str:
        solution = ''
        for i in range(len(s)):
            prefix = s[0:i]
            suffix = s[-len(prefix):]
            if prefix == suffix:
                solution = prefix
        return solution
