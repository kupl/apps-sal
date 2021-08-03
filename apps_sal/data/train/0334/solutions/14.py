from collections import defaultdict


class Solution:
    def minCost(self, s: str, cost: List[int]) -> int:
        cache = defaultdict(lambda: [float('-inf'), 0])
        last = None
        group = 0
        for cost, char in zip(cost, s):
            if char != last:
                last = char
                group += 1

            cache[group][0] = max(cache[group][0], cost)
            cache[group][1] += cost
        total = 0
        for maxCost, sum in list(cache.values()):
            total += sum - maxCost
        return total
