class Solution:
    def minCost(self, s: str, cost: List[int]) -> int:
        currentCost, totalCost, maxSoFar = 0, 0, 0
        for i in range(1, len(s)):
            if s[i] == s[i-1]:
                if currentCost == 0:
                    currentCost = cost[i-1] + cost[i]
                    maxSoFar = max(cost[i-1], cost[i])
                else:
                    currentCost += cost[i]
                    maxSoFar = max(maxSoFar, cost[i])
            else:
                if currentCost != 0:
                    totalCost += (currentCost - maxSoFar)
                    currentCost = 0
        if currentCost != 0:
            totalCost += (currentCost - maxSoFar)
        return totalCost
