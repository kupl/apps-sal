class Solution:

    def minCost(self, s: str, cost: List[int]) -> int:
        total = 0
        for i in range(1, len(s)):
            if s[i - 1] == s[i]:
                total += min(cost[i - 1], cost[i])
                cost[i] = max(cost[i - 1], cost[i])
        return total
