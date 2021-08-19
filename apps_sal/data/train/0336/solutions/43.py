class Solution:
    def minSteps(self, s: str, t: str) -> int:

        ds = collections.Counter(list(s))

        dt = collections.Counter(list(t))
        ans = 0
        # print(ds,dt)
        set_ = set(s + t)
       # print(set_)
        for i in set_:
            ans += abs(dt[i] - ds[i])
        return ans // 2
