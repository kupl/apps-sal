class Solution:
    def minSteps(self, s: str, t: str) -> int:
        ds, dt = defaultdict(int), defaultdict(int)

        for c in list(s):
            ds[c] += 1
        for c in list(t):
            dt[c] += 1

        res = 0
        for c in dt:
            res += max(0, dt[c] - ds[c])
        return res
