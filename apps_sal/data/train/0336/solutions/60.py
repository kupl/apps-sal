class Solution:

    def minSteps(self, s: str, t: str) -> int:
        d1 = {}
        for i in s:
            d1[i] = d1.get(i, 0) + 1
        d2 = {}
        for i in t:
            d2[i] = d2.get(i, 0) + 1
        c = 0
        for i in d1:
            k = d1[i] - d2.get(i, 0)
            if k > 0:
                c += abs(k)
        return c
