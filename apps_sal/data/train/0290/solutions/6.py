from functools import lru_cache


class Solution:

    def minCost(self, n: int, cuts: List[int]) -> int:
        lim = len(cuts)

        @lru_cache(None)
        def r(i, j):
            tmp = []
            for k in cuts:
                if k > i and k < j:
                    tmp.append(j - i + r(i, k) + r(k, j))
            if tmp == []:
                return 0
            return min(tmp)
        return r(0, n)
