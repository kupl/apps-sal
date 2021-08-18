import sys


class Solution:
    def minCost(self, s: str, cost: List[int]) -> int:
        total_cost = 0
        last = None
        cost_sum = 0
        max_cost = -sys.maxsize
        for i, v in zip(s, cost):
            if last == i:
                cost_sum += v
                max_cost = max(max_cost, v)
            else:
                if last is not None:
                    total_cost += (cost_sum - max_cost)
                max_cost = v
                cost_sum = v
                last = i
        total_cost += (cost_sum - max_cost)
        return total_cost
