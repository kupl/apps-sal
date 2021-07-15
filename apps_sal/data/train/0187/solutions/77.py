class Solution:
    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        if boardingCost * 4 <= runningCost:
            return -1
        
        rotate = 0
        out_rotate = 0
        
        cur_profit = 0
        max_profit = 0
        wait = 0
        for count in customers:
            rotate += 1
            wait += count
            cur_customer = min(4, wait)
            wait -= cur_customer
            cur_profit += (cur_customer * boardingCost - runningCost)
            if cur_profit > max_profit:
                max_profit = cur_profit
                out_rotate = rotate
        
        while wait:
            rotate += 1
            cur_customer = min(4, wait)
            wait -= cur_customer
            cur_profit += (cur_customer * boardingCost - runningCost)
            if cur_profit > max_profit:
                max_profit = cur_profit
                out_rotate = rotate
        
        return out_rotate
