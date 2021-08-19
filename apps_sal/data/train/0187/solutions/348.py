class Solution:

    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        if 4 * boardingCost <= runningCost:
            return -1
        curr_customers = 0
        curr_profit = 0
        max_profit = 0
        min_rotations = 0
        for (i, cus) in enumerate(customers):
            curr_customers += cus
            if curr_customers > 4:
                curr_profit += 4 * boardingCost - runningCost
                curr_customers -= 4
            else:
                curr_profit += curr_customers * boardingCost - runningCost
                curr_customers = 0
            if max_profit < curr_profit:
                max_profit = curr_profit
                min_rotations = i + 1
        (left_rounds, remainder) = divmod(curr_customers, 4)
        max_profit1 = max_profit
        max_profit2 = curr_profit + 4 * left_rounds * boardingCost - left_rounds * runningCost
        max_profit3 = curr_profit + curr_customers * boardingCost - (left_rounds + 1) * runningCost
        MAX = max(max_profit1, max_profit2, max_profit3)
        if MAX == max_profit1:
            min_rotations = min_rotations
        elif MAX == max_profit2:
            min_rotations = len(customers) + left_rounds
        else:
            min_rotations = len(customers) + left_rounds + 1
        return min_rotations if max_profit > 0 else -1
