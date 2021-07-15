class Solution:
    def minSteps(self, s: str, t: str) -> int:
        from collections import Counter
        counts = Counter(s)
        res = 0
        for c in t:
            if counts[c] > 0:
                counts[c] -= 1
            else:
                res += 1
        return res

