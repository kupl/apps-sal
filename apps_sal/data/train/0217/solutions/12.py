import math


class Solution:
    def subarrayBitwiseORs(self, A: List[int]) -> int:
        res = set([])
        tmp = []
        maximpact = 0
        for i in A:
            newtmp = []
            newtmp_set = set([])
            maximpact = max(maximpact, int(math.log(i, 2)) + 1 if i > 0 else 0)
            if i not in newtmp_set:
                newtmp_set.add(i)
                newtmp.append(i)
                res.add(i)
            if maximpact > 0:
                for j in tmp:
                    k = i | j
                    if k not in newtmp_set:
                        newtmp_set.add(k)
                        newtmp.append(k)
                    res.add(k)
                    if len(newtmp) >= maximpact:
                        break
            tmp = newtmp
        return len(res)
