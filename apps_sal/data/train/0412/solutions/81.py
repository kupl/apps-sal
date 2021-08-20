from math import comb


class Solution:

    def numRollsToTarget(self, d: int, f: int, target: int) -> int:
        dic = {}
        return self.helper(d, f, target, dic)

    def helper(self, d2, f2, target2, dic):
        if target2 == 0 and d2 == 0:
            return 1
        if (d2, f2, target2) in dic:
            return dic[d2, f2, target2]
        if target2 < d2 or d2 * f2 < target2:
            dic[d2, f2, target2] = 0
            return 0
        elif d2 == 1:
            dic[d2, f2, target2] = 1
            return 1
        tot = 0
        for i in range(0, d2 + 1):
            num_poss = self.helper(d2 - i, f2 - 1, target2 - i * f2, dic) * comb(d2, i)
            tot += num_poss % (10 ** 9 + 7)
        dic[d2, f2, target2] = tot % (10 ** 9 + 7)
        return tot % (10 ** 9 + 7)
