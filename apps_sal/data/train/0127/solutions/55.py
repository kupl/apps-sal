class Solution:

    def profitableSchemes(self, G: int, P: int, group: List[int], profit: List[int]) -> int:

        @lru_cache(None)
        def recur(hc, mp, ind):
            if hc < 0:
                return 0
            if ind >= len(profit):
                if mp <= 0:
                    return 1
                else:
                    return 0
            take = recur(hc - group[ind], max(0, mp - profit[ind]), ind + 1)
            skip = recur(hc, mp, ind + 1)
            return (take + skip) % (10 ** 9 + 7)
        return recur(G, P, 0)
