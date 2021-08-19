class Solution:

    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        max_profit = [-1, -1]

        def board_customers(customers, rotations):
            current_profit = customers * boardingCost - rotations * runningCost
            if current_profit > max_profit[0]:
                max_profit[0] = current_profit
                if current_profit > -1:
                    max_profit[1] = rotations
        r = 1
        waiting = 0
        total_customers = 0
        for i in range(len(customers) - 1):
            if customers[i] > 4:
                customers[i + 1] += customers[i] - 4
                customers[i] = 4
            total_customers += customers[i]
            board_customers(total_customers, r)
            r += 1
        waiting = customers[-1]
        while waiting:
            added = min(waiting, 4)
            total_customers += added
            board_customers(total_customers, r)
            waiting -= added
            r += 1
        return max_profit[1]
