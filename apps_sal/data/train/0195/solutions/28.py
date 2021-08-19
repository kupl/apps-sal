class Solution:

    def countTriplets(self, A: List[int]) -> int:
        d = {}
        res = 0
        for a in A:
            for b in A:
                t = a & b
                if t in d:
                    d[t] += 1
                else:
                    d[t] = 1
        for a in A:
            for (k, v) in list(d.items()):
                if a & k == 0:
                    res += v
        return res
