class Solution:
    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        max_profit = 0
        max_iter = 0
        cur_profit = 0
        available = 0
        i = 0
        while i < len(customers) or available > 0:
            if i < len(customers):
                available += customers[i]
            boarding = min(available, 4)
            cur_profit += boarding*boardingCost - runningCost*min(boarding,1)
            if cur_profit > max_profit:
                max_profit = cur_profit
                max_iter = i
            available -= boarding
            i += 1
        
        return (max_iter+1) if max_profit != 0 else -1
