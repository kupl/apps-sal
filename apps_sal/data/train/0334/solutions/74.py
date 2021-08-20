class Solution:

    def minCost(self, s: str, cost: List[int]) -> int:
        if len(s) == 0:
            return 0
        prev = 0
        min_cost = 0
        for (c, group) in itertools.groupby(list(s)):
            group = list(group)
            left = prev
            right = left + len(group) - 1
            prev = right + 1
            if len(group) == 1:
                continue
            x = max(cost[left:right + 1])
            total = sum(cost[left:right + 1])
            min_cost += total - x
        return min_cost
