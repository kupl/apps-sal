from functools import lru_cache


class Solution:

    def profitableSchemes(self, G: int, P: int, group: List[int], profit: List[int]) -> int:

        @lru_cache(None)
        def dfs(index, curr_profit, members_left):
            if index == len(profit) or members_left == 0:
                return curr_profit == 0
            res = 0
            res += dfs(index + 1, curr_profit, members_left)
            if members_left - group[index] >= 0:
                res += dfs(index + 1, max(0, curr_profit - profit[index]), members_left - group[index])
            return res % (10 ** 9 + 7)
        return dfs(0, P, G)
