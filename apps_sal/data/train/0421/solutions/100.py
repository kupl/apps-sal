class Solution:

    def lastSubstring(self, s: str) -> str:
        last_c = max(s)
        last_str = s
        for i in range(len(s)):
            if s[i] == last_c and s[i:] > last_str:
                last_str = s[i:]
        return last_str
