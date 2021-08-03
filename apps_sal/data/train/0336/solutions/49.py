class Solution:
    def minSteps(self, s: str, t: str) -> int:
        if len(s) == len(t) <= 50000 and s.islower() and t.islower():
            if collections.Counter(s) == collections.Counter(t):
                return 0
            diff = collections.Counter(s) - collections.Counter(t)
            return sum(diff.values())
        else:
            return 0
