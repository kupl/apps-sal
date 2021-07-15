class Solution:
    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        max_profit = 0
        answ = -1
        waiting = 0
        profit = 0
        i = 0
        
        for i in range(len(customers)):
            # print(\"{} :: max:{} profit:{} answ:{} waiting:{}\".format(i, max_profit, profit, answ, waiting))
            waiting += customers[i]
            if waiting >= 4:
                profit += 4*boardingCost - runningCost
                waiting -= 4
            elif waiting > 0:
                profit += waiting*boardingCost - runningCost
                waiting = 0
            else:
                profit -= runningCost
            
            if max_profit < profit:
                max_profit = profit
                answ = i + 1
                
        while waiting > 0:
            i += 1
            if waiting >= 4:
                profit += 4*boardingCost - runningCost
                waiting -= 4
            elif waiting > 0:
                profit += waiting*boardingCost - runningCost
                waiting = 0
            else:
                profit -= runningCost
            
            if max_profit < profit:
                max_profit = profit
                answ = i + 1
                
        return answ

