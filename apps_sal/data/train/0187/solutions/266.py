class Solution:

    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        if boardingCost * 4 <= runningCost:
            return -1
        profit = 0
        num_waiting_customers = 0
        max_profit = 0
        ans = -1
        i = 0
        while i < len(customers) or num_waiting_customers > 0:
            num_waiting_customers += customers[i] if i < len(customers) else 0
            num_boarding = min(num_waiting_customers, 4)
            num_waiting_customers -= num_boarding
            profit += num_boarding * boardingCost - runningCost
            if profit > max_profit:
                ans = i + 1
                max_profit = profit
            i += 1
        return ans
