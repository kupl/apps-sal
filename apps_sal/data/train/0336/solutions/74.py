class Solution:

    def minSteps(self, s: str, t: str) -> int:
        if s == t:
            return 0
        s_d = collections.Counter(s)
        for c in t:
            if c in s_d and s_d[c] > 0:
                s_d[c] -= 1
        return sum(s_d.values())
