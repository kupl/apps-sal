class Solution:       
    def lastSubstring(self, s: str) -> str:
        max_char = max(s)
        return max(s[i:] for i, c in enumerate(s) if c == max_char)

