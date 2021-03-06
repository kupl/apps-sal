class Solution:

    def minCost(self, s: str, cost: List[int]) -> int:
        out = 0
        for i in range(len(s) - 1):
            if s[i] == s[i + 1]:
                out += min(cost[i], cost[i + 1])
                cost[i] = max(cost[i], cost[i + 1])
                cost[i + 1] = max(cost[i], cost[i + 1])
        return out
