class Solution:

    def minOperationsMaxProfit(self, customers, boardingCost, runningCost):
        if 4 * boardingCost <= runningCost:
            return -1
        total = sum(customers)
        maxProfit = -1
        maxRotate = 0
        accuProfit = 0
        rotate = 0
        i = 0
        prev = 0
        while i < len(customers):
            prev = accuProfit
            if customers[i] <= 4:
                accuProfit += customers[i] * boardingCost
                customers[i] = 0
                total -= customers[i]
            else:
                accuProfit += 4 * boardingCost
                customers[i] -= 4
                total -= 4
            rotate += 1
            accuProfit -= runningCost
            if maxProfit < accuProfit:
                maxProfit = accuProfit
                maxRotate = rotate
            if i + 1 < len(customers):
                customers[i + 1] += customers[i]
                customers[i] = 0
            if customers[i] == 0:
                i += 1
        return -1 if maxProfit < 0 else maxRotate
