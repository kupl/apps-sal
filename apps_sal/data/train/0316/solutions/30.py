class Solution:
    def longestPrefix(self, s: str) -> str:
        n = len(list(s))
        for i in range(0, n):
            if s[0:i] == s[n - i:n]:
                result = s[0:i]
        return result
