class Solution:
    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        if 4 * boardingCost < runningCost:
            return -1

        #
        rotate = 0
        max_profit = float('-inf')
        max_profit_for = rotate
        total_customer = 0
        while True:
            rotate += 1
            current_customer = min(4, customers[rotate - 1])
            total_customer += current_customer
            if len(customers) <= rotate and current_customer <= 0:
                return max_profit_for
            if len(customers) > rotate:
                customers[rotate] += max(0, customers[rotate - 1] - current_customer)
            else:
                customers.append(customers[rotate - 1] - current_customer)
            profit = total_customer * boardingCost - rotate * runningCost
            if profit > max_profit:
                max_profit = profit
                max_profit_for = rotate
