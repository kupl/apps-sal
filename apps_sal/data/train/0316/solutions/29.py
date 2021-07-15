class Solution:
    def longestPrefix(self, s: str) -> str:
        best = ''
        
        for i in range(1, len(s)):
            pattern = s[:i]
            if s.startswith(pattern) and s.endswith(pattern):
                best = pattern
        
        return best
