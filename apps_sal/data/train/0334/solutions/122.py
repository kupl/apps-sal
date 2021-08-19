class Solution:

    def minCost(self, s: str, cost: List[int]) -> int:
        result = 0
        p1 = 0
        while p1 < len(s) - 1:
            if s[p1] == s[p1 + 1]:
                p2 = p1
                (totalSum, maxCost) = (cost[p2], cost[p2])
                while p2 < len(s) - 1 and s[p2] == s[p2 + 1]:
                    p2 += 1
                    totalSum += cost[p2]
                    maxCost = max(maxCost, cost[p2])
                result += totalSum - maxCost
                p1 = p2 + 1
            else:
                p1 += 1
        return result
