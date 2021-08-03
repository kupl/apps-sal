class Solution:
    def minSteps(self, s: str, t: str) -> int:
        sf = Counter(s)
        tf = Counter(t)
        return sum((tf - sf).values())
