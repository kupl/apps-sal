class Solution:
    def longestPrefix(self, s: str) -> str:
        res = ''
        i, j = 0, len(s) - 1
        while i < len(s)-1:
            if s[:i+1] == s[j:]:
                res = s[:i+1]
            i += 1
            j -= 1
        return res

