class Solution:

    def minCost(self, s: str, cost: List[int]) -> int:
        cur_max = cur_cost = 0
        total = 0
        for i in range(1, len(s)):
            if s[i] == s[i - 1]:
                if cur_cost == 0:
                    cur_cost = cost[i] + cost[i - 1]
                    cur_max = max(cost[i], cost[i - 1])
                else:
                    cur_cost += cost[i]
                    cur_max = max(cur_max, cost[i])
            elif cur_cost != 0:
                total += cur_cost - cur_max
                cur_cost = cur_max = 0
        if cur_cost != 0:
            total += cur_cost - cur_max
        return total
