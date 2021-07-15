class Solution:
    def minCost(self, s: str, cost: List[int]) -> int:
        res, last = 0, None
        max_cost = float('-inf')
        cur_cost = 0
        for i, c in enumerate(s):
            if c == last:
                if cur_cost == 0:
                    max_cost = max(cost[i - 1], max_cost)
                    cur_cost += cost[i - 1]
                cur_cost += cost[i]
                max_cost = max(cost[i], max_cost)
            else:
                if cur_cost > 0:
                    res += cur_cost - max_cost
                    cur_cost = 0
                    max_cost = float('-inf')
            # print(i, c, last, cur_cost, max_cost)
            last = c
        if cur_cost > 0:
            res += cur_cost - max_cost
        return res
