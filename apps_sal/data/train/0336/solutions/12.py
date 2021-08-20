class Solution:

    def minSteps(self, s: str, t: str) -> int:
        cs = collections.Counter(s)
        ct = collections.Counter(t)
        for x in s:
            if x in ct and ct[x] > 0:
                ct[x] -= 1
                cs[x] -= 1
        return sum(cs.values())
