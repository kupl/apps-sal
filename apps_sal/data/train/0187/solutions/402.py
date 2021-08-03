class Solution:
    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        wait = 0
        profit = 0
        max_profit = 0
        max_index = -1

        i = 0
        while True:
            if i >= len(customers) and wait == 0:
                break
            if i < len(customers):
                cus = customers[i]
            else:
                cus = 0
            profit += min(4, cus + wait) * boardingCost - runningCost
            wait = max(cus + wait - 4, 0)
            if profit > max_profit:
                max_profit = profit
                max_index = i + 1
            i += 1

        return max_index
