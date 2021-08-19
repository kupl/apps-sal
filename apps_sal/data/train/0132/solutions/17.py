class Solution:

    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        cost = [0 for j in range(366)]
        for i in range(len(cost)):
            if i in days:
                cost[i] = min((cost[i - 1] if i - 1 >= 0 else 0) + costs[0], (cost[i - 7] if i - 7 >= 0 else 0) + costs[1], (cost[i - 30] if i - 30 >= 0 else 0) + costs[2])
            else:
                cost[i] = cost[max(i - 1, 0)]
        return cost[365]
