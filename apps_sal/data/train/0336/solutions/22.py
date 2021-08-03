class Solution:
    def minSteps(self, s: str, t: str) -> int:
        # ct = Counter(t)
        # cs = Counter(s)
        ct = {}
        cs = {}
        for i in range(len(s)):
            ct.update({t[i]: ct.get(t[i], 0) + 1})
            cs.update({s[i]: cs.get(s[i], 0) + 1})
        c = 0
        for k, v in cs.items():
            r = v - ct.get(k, 0)
            c += r if r > 0 else 0
        return c
