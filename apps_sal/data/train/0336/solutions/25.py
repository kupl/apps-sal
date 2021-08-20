from collections import Counter


class Solution:

    def minSteps(self, s: str, t: str) -> int:
        c = Counter(s)
        for char in t:
            if char in c:
                c[char] = max(0, c[char] - 1)
        return sum(c.values())
