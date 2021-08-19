class Solution:
    def profitableSchemes(self, G: int, P: int, group: List[int], profit: List[int]) -> int:

        @lru_cache(None)
        def recur(hc, mp, ind):

            # no enough people left
            if hc < 0:
                return 0

            # end of tasks
            if ind >= len(profit):
                # print(\"hc mp ind\", hc, mp, ind)
                if mp <= 0:
                    return 1
                else:
                    return 0

            # take this crime
            take = recur(hc - group[ind], max(0, mp - profit[ind]), ind + 1)
            # skip this crime
            skip = recur(hc, mp, ind + 1)

            return (take + skip) % (10**9 + 7)

        return recur(G, P, 0)
