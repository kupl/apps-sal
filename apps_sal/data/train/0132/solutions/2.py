class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:

        @lru_cache(None)
        def recur(day):
            if day > 365:
                return 0
            elif day in days:

                ret = math.inf
                for c, d in zip(costs, [1, 7, 30]):
                    ret = min(ret, c + recur(day + d))
                return ret

            else:
                return recur(day + 1)

        return recur(0)
