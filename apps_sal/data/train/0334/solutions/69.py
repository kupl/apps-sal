class Solution:

    def minCost(self, s: str, cost: List[int]) -> int:
        consecutive_log = []
        consecutive_tuple = [-1, -1, -1]
        previous_e = -1
        for (i, e) in enumerate(s):
            if e != previous_e:
                consecutive_log.append(consecutive_tuple)
                consecutive_tuple = [e, i, i]
                previous_e = e
            else:
                consecutive_tuple[2] = i
                previous_e = e
        consecutive_log.append(consecutive_tuple)
        total_cost = 0
        for log in consecutive_log:
            if log[1] != log[2]:
                selected_costs = cost[log[1]:log[2] + 1]
                max_cost = max(selected_costs)
                selected_costs.remove(max_cost)
                total_cost += sum(selected_costs)
        return total_cost
