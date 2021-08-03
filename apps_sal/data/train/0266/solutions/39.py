class Solution:
    def numSplits(self, s: str) -> int:

        c = Counter(s)
        res = 0

        d = dict()
        for i, v in enumerate(s):
            if v not in d:
                d[v] = 1
            else:
                d[v] += 1
            c[v] -= 1
            if c[v] == 0:
                del c[v]
            if len(c) == len(d):
                res += 1

        return res
