class Solution:

    def lastSubstring(self, s: str) -> str:
        prev = s[0]
        max_store = []
        max_s = max(s)
        for i in range(len(s)):
            if s[i] == max_s:
                if s[i:] > prev:
                    prev = s[i:]
        return prev
