class Solution:

    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        min_costs = [-1 for i in range(days[-1])]
        if 1 in days:
            min_costs[0] = min(costs)
        else:
            min_costs[0] = 0
        return self.helper(days, costs, min_costs, days[-1] - 1)

    def helper(self, days: List[int], costs: List[int], min_costs: List[int], i) -> int:
        if i == 0:
            return min_costs[0]
        if i < 0:
            return 0
        if i + 1 not in days:
            min_costs[i] = self.helper(days, costs, min_costs, i - 1)
        if min_costs[i] != -1:
            return min_costs[i]
        c_1 = self.helper(days, costs, min_costs, i - 1)
        c_7 = self.helper(days, costs, min_costs, i - 7)
        c_30 = self.helper(days, costs, min_costs, i - 30)
        min_costs[i] = min(c_1 + costs[0], c_7 + costs[1], c_30 + costs[2])
        return min_costs[i]


"\nmin_cost(1) = min(costs[0], costs[1], costs[2])\n\nmin_cost(i) = min cost of traveling up to the days[i]th day.\nmin_cost(0) = min(costs[0], costs[1], costs[2])\nmin_cost(i < 0) = min(costs[0], costs[1], costs[2])\nmin_cost(i) = (min_cost(i-1) + costs[0], min_cost(i-7) + costs[1], min_cost(i-30) + costs[2])\n\n\n\n\nmin_cost(i) = minimum cost of traveling i days, (1-indexed).\nmin_cost(1) = min(costs[0], costs[1], costs[2])\nmin_cost(i < 1) = min(costs[0], costs[1], costs[2]) ???\nmin_cost(i) = (min_cost(i-1) + costs[0], min_cost(i-7) + costs[1], min_cost(i-30) + costs[2]) \n\n**** This doesn't account for the case where a longer pass may be cheaper.\n\n\n"
