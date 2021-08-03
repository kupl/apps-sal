class Solution:
    def profitableSchemes(self, G: int, P: int, group: List[int], profit: List[int]) -> int:
        @lru_cache(None)
        def dp(i, total_profit, member_left):
            if i == len(profit) or member_left <= 0:
                return 0
            take = 0
            if member_left >= group[i]:
                take += (1 if profit[i] + total_profit >= P else 0)
                #take += dp(i+1, total_profit + profit[i], member_left-group[i])
                take += dp(i + 1, min(P, total_profit + profit[i]), max(0, member_left - group[i]))
            skip = dp(i + 1, total_profit, member_left)
            return take + skip
        return dp(0, 0, G) % (10**9 + 7)
