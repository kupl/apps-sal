class Solution:
    def longestPrefix(self, s: str) -> str:
        ans = ''
        for i in range(len(s)):
            if s[:i] == s[-i:] and len(s[:i]) >= len(ans):
                ans = s[:i]
        return ans
