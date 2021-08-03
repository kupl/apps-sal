class Solution:
    def longestPrefix(self, s: str) -> str:
        if len(s) < 2:
            return ''
        length = len(s)
        res = ''
        for i in range(len(s) - 1):
            if s[: i + 1] == s[length - i - 1:]:
                res = s[: i + 1]
        return res
