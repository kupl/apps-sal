class Solution:
    def minSteps(self, s: str, t: str) -> int:
        cs = collections.Counter(s)
        ct = collections.Counter(t)
        diff = 0
        for i in ct:
            if i in cs:
                if ct[i] > cs[i]:
                    diff += ct[i] - cs[i]
            else:
                diff += ct[i]
        return diff
