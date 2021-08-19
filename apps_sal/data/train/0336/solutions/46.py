class Solution:

    def minSteps(self, s: str, t: str) -> int:
        s = list(s)
        ds = collections.Counter(s)
        t = list(t)
        dt = collections.Counter(t)
        ans = 0
        set_ = set(s + t)
        for i in set_:
            ans += abs(dt[i] - ds[i])
        return ans // 2
