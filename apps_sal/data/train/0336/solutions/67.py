class Solution:

    def minSteps(self, s: str, t: str) -> int:
        from collections import defaultdict
        s_f = defaultdict(int)
        t_f = defaultdict(int)
        c = 0
        for x in s:
            s_f[x] += 1
        for y in t:
            t_f[y] += 1
        for z in s_f:
            s_i = s_f[z] - t_f[z]
            if s_i > 0:
                c += s_i
        return c
