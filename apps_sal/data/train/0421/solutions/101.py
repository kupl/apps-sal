class Solution:

    def lastSubstring(self, s: str) -> str:
        mx = max(s)
        prev = ''
        for i in range(len(s)):
            if s[i] == mx:
                if s[i:] > prev:
                    prev = s[i:]
        return prev
