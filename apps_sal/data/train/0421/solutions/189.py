class Solution:
    def lastSubstring(self, s: str) -> str:
        return max(s[i:] for i in range(len(s)))
