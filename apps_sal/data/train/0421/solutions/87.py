class Solution:
    def lastSubstring(self, s: str) -> str:
        max_ord = 0
        if s.count(s[0]) == len(s):
            return s
        for i in range(len(s)):
            max_ord = max(max_ord, ord(s[i]))
        start = chr(max_ord)
        result = ''
        for i in range(s.count(start)):
            substr = s[s.find(start):]
            result = max(result, substr)
            s = s[s.find(start) + 1:]
        return result
