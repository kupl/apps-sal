class Solution:

    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        maxProfits = 0
        minOperations = -1
        currentOperations = 0
        currentProfits = 0
        customers_waiting = 0
        customers_boarding = 0
        for i in range(len(customers)):
            customers_waiting += customers[i]
            if customers_waiting <= 4:
                customers_boarding = customers_waiting
                customers_waiting = 0
            else:
                customers_boarding = 4
                customers_waiting -= 4
            currentOperations += 1
            currentProfits += customers_boarding * boardingCost - runningCost
            if currentProfits > maxProfits:
                maxProfits = currentProfits
                minOperations = currentOperations
        while customers_waiting != 0:
            if customers_waiting <= 4:
                customers_boarding = customers_waiting
                customers_waiting = 0
            else:
                customers_boarding = 4
                customers_waiting -= 4
            currentOperations += 1
            currentProfits += customers_boarding * boardingCost - runningCost
            if currentProfits > maxProfits:
                maxProfits = currentProfits
                minOperations = currentOperations
        return minOperations
