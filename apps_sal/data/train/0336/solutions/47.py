from collections import Counter


class Solution:

    def minSteps(self, s: str, t: str) -> int:
        sc = Counter(s)
        tc = Counter(t)
        c = 0
        for i in tc:
            c += tc[i]
        for i in tc:
            if i in sc:
                if tc[i] <= sc[i]:
                    c -= tc[i]
                elif tc[i] > sc[i]:
                    c -= sc[i]
        return c
