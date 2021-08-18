class Solution:
    def longestPrefix(self, s: str) -> str:

        i = 1
        ans = ''
        while i < len(s):
            if s[0:i] == s[len(s) - i:]:
                ans = s[0:i]
            i += 1
        return ans
