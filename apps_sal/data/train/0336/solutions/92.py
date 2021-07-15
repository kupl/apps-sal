class Solution:
    def minSteps(self, s: str, t: str) -> int:
        return sum(map(abs, (Counter(s) - Counter(t)).values() ))
