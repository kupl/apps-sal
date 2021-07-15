class Solution:
    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        
        waiting = 0
        onBoard = []
        profit = 0
        maxProfit = 0
        ans = 0
        for i, customer in enumerate(customers):
            waiting += customer
            if waiting >= 4:
                profit += (4*boardingCost - runningCost)
                waiting -= 4
                onBoard.append(4)
            else:
                profit += (waiting*boardingCost - runningCost)
                onBoard.append(waiting)
                waiting = 0
            freeRound = 3
            j = 1
            while j <= min(i, 3) and onBoard[-j] == 0:
                j += 1
                freeRound -= 1
            stopNowProfit = profit - freeRound*runningCost
            if stopNowProfit > maxProfit:
                maxProfit = stopNowProfit
                ans = i+1
                
        while waiting > 0:
            i += 1
            if waiting >= 4:
                profit += (4*boardingCost - runningCost)
                waiting -= 4
                onBoard.append(4)
            else:
                profit += (waiting*boardingCost - runningCost)
                onBoard.append(waiting)
                waiting = 0
            freeRound = 3
            j = 1
            while j <= min(i, 3) and onBoard[-j] == 0:
                j += 1
                freeRound -= 1
            stopNowProfit = profit - freeRound*runningCost
            if stopNowProfit > maxProfit:
                maxProfit = stopNowProfit
                ans = i+1     
        if ans == 0:
            return -1
        return ans
            

