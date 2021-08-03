from collections import Counter


class Solution:
    def minSteps(self, s: str, t: str) -> int:
        d1 = Counter(s)
        d2 = Counter(t)
        res = 0
        if d1 == d2:
            return 0

        for i in s:
            if i in d2:
                d1[i] -= 1
                d2[i] -= 1
                if d1[i] == 0:
                    del d1[i]
                if d2[i] == 0:
                    del d2[i]

        for key, val in list(d2.items()):
            res += val
        return res
