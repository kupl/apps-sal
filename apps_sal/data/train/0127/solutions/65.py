class Solution:
    def profitableSchemes(self, G: int, P: int, group: List[int], profit: List[int]) -> int:
        # knapsack
        @lru_cache(None)
        def dp(i, ppl_left, money):
            if ppl_left < 0:
                return 0
            if i == len(group):
                return 0
            ret = 0
            # do or dont do this crime
            ret += dp(i + 1, ppl_left, money)
            # check if doing this crime can get me above P
            if money + profit[i] >= P and ppl_left >= group[i]:
                ret += 1
            ret += dp(i + 1, ppl_left - group[i], min(money + profit[i], P))
            return ret % (10**9 + 7)
        return dp(0, G, 0)
