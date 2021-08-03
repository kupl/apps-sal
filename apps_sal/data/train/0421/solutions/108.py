class Solution:
    def lastSubstring(self, s: str) -> str:
        max_ = max(s)
        max_positions = [i for i, c in enumerate(s) if c == max_]
        return max(s[i:] for i in max_positions)
