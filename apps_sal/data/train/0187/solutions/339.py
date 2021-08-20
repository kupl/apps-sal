import math


class Solution:

    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        (profit, bestIteration, customerCount, iteration, boarding) = (0, 0, 0, 0, 0)
        for i in range(len(customers)):
            customerCount = customerCount + customers[i]
            iteration = iteration + 1
            boarding = boarding + min(customerCount, 4)
            customerCount = customerCount - min(customerCount, 4)
            if boarding * boardingCost - iteration * runningCost > profit:
                profit = boarding * boardingCost - iteration * runningCost
                bestIteration = iteration
        while customerCount > 0:
            iteration = iteration + 1
            boarding = boarding + min(customerCount, 4)
            customerCount = customerCount - min(customerCount, 4)
            if boarding * boardingCost - iteration * runningCost > profit:
                profit = boarding * boardingCost - iteration * runningCost
                bestIteration = iteration
        if profit == 0:
            return -1
        return bestIteration
