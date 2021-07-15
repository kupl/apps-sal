class Solution:
    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        if boardingCost * 4 <= runningCost or len(customers) == 0:
            return -1
        left = 0
        profit = 0
        res = 0
        max_profit = 0
        idx = 0
        r = 0
        while idx < len(customers) or left > 0:
            r += 1
            if idx < len(customers):
                left += customers[idx]
                idx += 1
            
            if left < 4:
                profit += left * boardingCost - runningCost
                left = 0
            else:
                left -= 4
                profit += 4 * boardingCost - runningCost
                
            if profit > max_profit:
                max_profit = profit
                res = r
        return res
