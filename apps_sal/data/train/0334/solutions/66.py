class Solution:
    def minCost(self, s: str, cost: List[int]) -> int:
        if len(s) == 1:
            return 0
        pre_c = s[0]
        pre_cost_max = cost[0]
        count = 0
        for c, _cost in zip(s[1:], cost[1:]):
            if c == pre_c:
                count += min(pre_cost_max, _cost)
                pre_cost_max = max(pre_cost_max, _cost)
            else:
                pre_c = c
                pre_cost_max = _cost
        return count
