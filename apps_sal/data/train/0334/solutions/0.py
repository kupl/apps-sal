class Solution:
    def minCost(self, s: str, cost: List[int]) -> int:
        delete_cost = 0
        last = 0
        for i in range(1, len(s)):
            if s[last] == s[i]:
                if cost[last] < cost[i]:
                    delete_cost += cost[last]
                    last = i
                else:
                    delete_cost += cost[i]
            else:
                last = i
        return delete_cost
