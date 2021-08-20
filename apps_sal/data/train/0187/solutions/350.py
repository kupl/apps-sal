class Solution:

    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        total_queue = 0
        idx = 0
        curr_costs = 0
        max_costs = float('-inf')
        max_idx = 0
        while total_queue or idx < len(customers):
            curr_customers = 0
            if idx < len(customers):
                curr_customers = min(4, customers[idx])
                total_queue += max(0, customers[idx] - 4)
            if curr_customers < 4 and total_queue:
                diff = 4 - curr_customers
                curr_customers += min(diff, total_queue)
                total_queue = max(0, total_queue - diff)
            idx += 1
            curr_costs += boardingCost * curr_customers - runningCost
            if curr_costs > max_costs:
                max_idx = idx
                max_costs = curr_costs
        return max_idx if max_costs > 0 else -1
