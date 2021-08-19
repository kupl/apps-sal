class Solution:

    def lastSubstring(self, s: str) -> str:
        res = s
        for i in range(1, len(s)):
            if s[i:] > res:
                res = s[i:]
        return res
