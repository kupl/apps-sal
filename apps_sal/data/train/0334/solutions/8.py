class Solution:

    def minCost(self, s: str, cost: List[int]) -> int:
        (l, total) = (0, 0)
        for r in range(1, len(cost)):
            if s[r] == s[l]:
                if cost[r] > cost[l]:
                    total += cost[l]
                    l = r
                else:
                    total += cost[r]
            else:
                l = r
        return total
