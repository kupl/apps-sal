class Solution:

    def minSteps(self, s: str, t: str) -> int:
        d1 = collections.Counter(s)
        d2 = collections.Counter(t)
        return sum((d1 - d2).values())
