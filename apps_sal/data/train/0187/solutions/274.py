class Solution:
    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        i = 1
        waiting, onBoard, result, maxProfit = customers[0], 0, -1, 0
        while i < len(customers) or waiting > 0:
            newToOnboard = min(4, waiting)

            waiting -= newToOnboard
            onBoard += newToOnboard

            profit = onBoard * boardingCost - i * runningCost

            if(profit > maxProfit):
                maxProfit = profit
                result = i
            if(i < len(customers)):
                waiting += customers[i]
            i += 1
        return result
