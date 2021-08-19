class Solution:

    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        count = 0
        max_profit = 0
        profit = 0
        rot = -1
        i = 0
        while count > 0 or i < len(customers):
            if i < len(customers):
                new_customers = customers[i]
                count += new_customers
            if count >= 4:
                count -= 4
                profit += 4 * boardingCost - runningCost
            else:
                profit += count * boardingCost - runningCost
                count = 0
            i += 1
            if profit > max_profit:
                max_profit = profit
                rot = i
        return rot
