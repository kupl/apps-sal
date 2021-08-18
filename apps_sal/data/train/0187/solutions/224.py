class Solution:
    def minOperationsMaxProfit(self, customers, boardingCost, runningCost):
        if 4 * boardingCost <= runningCost:
            return -1
        maxProfit = -1
        maxRotate = 0
        accuProfit = 0
        rotate = 0
        boardingPool = 0

        i = 0
        while i < len(customers) or boardingPool > 0:
            if i < len(customers):
                boardingPool += customers[i]
                i += 1

            currBoarding = min(4, boardingPool)
            boardingPool -= currBoarding
            accuProfit += currBoarding * boardingCost

            rotate += 1
            accuProfit -= runningCost
            if maxProfit < accuProfit:
                maxProfit = accuProfit
                maxRotate = rotate

        return -1 if maxProfit < 0 else maxRotate
