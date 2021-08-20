class Solution:

    def minCost(self, s: str, cost: List[int]) -> int:
        res = 0
        for (k, g) in itertools.groupby(zip(s, cost), key=lambda p: p[0]):
            g = list(g)
            if len(g) > 1:
                costs = [t[1] for t in g]
                res += sum(costs) - max(costs)
        return res
