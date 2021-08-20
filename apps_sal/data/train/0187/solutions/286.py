class Solution:

    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        max_profit = remainder_customers = steps = 0
        res = []
        for customer in customers:
            remainder_customers += customer
            if remainder_customers > 4:
                remainder_customers -= 4
                max_profit += 4 * boardingCost - runningCost
            else:
                max_profit += remainder_customers * boardingCost - runningCost
                remainder_customers = 0
            steps += 1
            res.append((max_profit, steps))
        while remainder_customers > 0:
            if remainder_customers > 4:
                remainder_customers -= 4
                max_profit += 4 * boardingCost - runningCost
            else:
                max_profit += remainder_customers * boardingCost - runningCost
                remainder_customers = 0
            steps += 1
            res.append((max_profit, steps))
        res.sort(key=lambda x: (-x[0], x[1]))
        return -1 if res[0][0] < 0 else res[0][1]
