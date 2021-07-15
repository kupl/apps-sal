class Solution:
    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        i = 1 # start at 1
        waiting, onBoard, result, maxProfit  = customers[0],  0, -1, 0
        while i < len(customers) or waiting > 0:
            newToOnboard = min(4, waiting) # get 4 or remainder + current passangers

            waiting -= newToOnboard # remove people waiting
            onBoard += newToOnboard # add people to go

            profit = onBoard*boardingCost - i*runningCost # get profit of all to go

            if(profit>maxProfit): # if profit is over max then reset the maxProfit
                maxProfit = profit
                result = i
            if(i<len(customers)): waiting +=customers[i] # stop adding customers once we finish list
            i +=  1
        return result

