class Solution:
    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:

        profits = []
        waiting_customers = 0
        cur_profit = 0

        for count in customers:
            waiting_customers += count
            boarding_customers = min(4, waiting_customers)
            cur_profit += boardingCost * boarding_customers - runningCost
            profits.append(cur_profit)
            waiting_customers -= boarding_customers

        while waiting_customers > 0:
            boarding_customers = min(4, waiting_customers)
            cur_profit += boardingCost * boarding_customers - runningCost
            profits.append(cur_profit)
            waiting_customers -= boarding_customers

        index = -1
        max_profit = 0
        for i in range(len(profits)):
            if profits[i] > max_profit:
                index = i
                max_profit = profits[i]

        if index == -1:
            return -1
        return index + 1
