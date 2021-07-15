class Solution:
    def minCost(self, s: str, cost: List[int]) -> int:
        total = 0
        for i in range(1,len(s)):
            if s[i] == s[i-1]:
                total += min(cost[i],cost[i-1])
                cost[i] = max(cost[i],cost[i-1])
        return total
