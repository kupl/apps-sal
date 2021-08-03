from collections import Counter


class Solution:
    def minSteps(self, s: str, t: str) -> int:
        c1, c2 = map(Counter, (s, t))

        return sum(1 for _ in (c1 - c2).elements())
