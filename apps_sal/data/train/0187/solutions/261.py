class Solution:
    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        totalServed = 0
        step = 0
        customerWaiting = 0
        highestProfit = -1
        for i in range(len(customers)):
            customerGroup = customers[i]
            customerWaiting += customerGroup
            willBeServed = min(customerWaiting, 4)
            totalServed += willBeServed
            profit = totalServed * boardingCost - (i + 1) * runningCost
            if profit > highestProfit:
                highestProfit = profit
                step = i + 1
            customerWaiting -= willBeServed
        i += 1
        while customerWaiting > 0:
            willBeServed = min(customerWaiting, 4)
            totalServed += willBeServed
            profit = totalServed * boardingCost - (i + 1) * runningCost
            if profit > highestProfit:
                highestProfit = profit
                step = i + 1
            customerWaiting -= willBeServed
            i += 1
        return -1 if highestProfit < 0 else step
        
            

