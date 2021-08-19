class Solution:

    def minSteps(self, s: str, t: str) -> int:
        from collections import Counter
        (s, t) = map(Counter, [s, t])
        return sum((max(s[c] - t[c], 0) for c in s))
