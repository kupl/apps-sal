class Solution:
    def longestPrefix(self, s: str) -> str:
        ans = 0
        for l in range(len(s)):
            if s[:l] == s[-l:]:
                ans = l
        
        return s[:ans]
