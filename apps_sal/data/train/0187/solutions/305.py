class Solution:

    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        bestProfit = -1
        bestNumRotations = -1
        currentCustomersWaiting = 0
        currentProfit = 0
        numRotations = 1

        def spin(newCustomers):
            nonlocal currentCustomersWaiting, currentProfit, numRotations, bestProfit, bestNumRotations
            currentCustomersWaiting += newCustomers
            customersBoardingNow = min(4, currentCustomersWaiting)
            currentProfit += customersBoardingNow * boardingCost - runningCost
            if currentProfit > bestProfit:
                bestProfit = currentProfit
                bestNumRotations = numRotations
            currentCustomersWaiting -= customersBoardingNow
            numRotations += 1
        for currentNewCustomers in customers:
            spin(currentNewCustomers)
        while currentCustomersWaiting:
            spin(0)
        return bestNumRotations
