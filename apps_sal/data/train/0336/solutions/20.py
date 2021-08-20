class Solution:

    def minSteps(self, s: str, t: str) -> int:
        res = 0
        s = list(s)
        t = list(t)
        d1 = dict()
        d2 = dict()
        for i in s:
            if i in d1.keys():
                d1[i] += 1
            else:
                d1[i] = 1
        for i in t:
            if i in d2.keys():
                d2[i] += 1
            else:
                d2[i] = 1
        res = 0
        for i in d1.keys():
            if i in d2.keys() and d2[i] < d1[i]:
                res += d1[i] - d2[i]
            elif i not in d2.keys():
                res += d1[i]
        return res
