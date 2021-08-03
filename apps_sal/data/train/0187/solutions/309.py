class Solution:
    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        bestProfit = 0
        bestRotation = 0
        waiting = 0
        income = 0
        cost = 0
        rotations = 0
        for i in range(len(customers)):
            if income - cost > bestProfit:
                bestRotation = rotations
                bestProfit = income - cost
            waiting += customers[i]
            newCustomers = min(waiting, 4)
            waiting -= newCustomers
            income += newCustomers * boardingCost
            cost += runningCost
            rotations += 1
        while waiting > 0:
            if income - cost > bestProfit:
                bestRotation = rotations
                bestProfit = income - cost
            newCustomers = min(waiting, 4)
            waiting -= newCustomers
            income += newCustomers * boardingCost
            cost += runningCost
            rotations += 1
        if income - cost > bestProfit:
            bestRotation = rotations
            bestProfit = income - cost
        if bestProfit == 0:
            return -1
        else:
            return bestRotation
