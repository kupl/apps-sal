class Solution:
    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:

        totalCustomers = sum(customers)
        rotation = totalCustomers // 4
        totalRotation = rotation if totalCustomers % 4 == 0 else rotation + 1
        totalRotation = max(totalRotation, len(customers))
        totalRotationCost = totalRotation * runningCost

        earning = rotation * 4 * boardingCost
        remain = totalCustomers % 4
        if remain != 0:
            earning += (remain * boardingCost)
        profit = earning - totalRotationCost

        if profit <= 0:
            return -1

        maxProfit = 0
        currentCost = 0
        remainingCustomer = sum(customers)
        highestRotation = 0
        i = 0
        total = 0
        while total > 0 or i < len(customers):
            if i < len(customers):
                total += customers[i]

            prev = currentCost
            if total >= 4:
                currentCost += (4 * boardingCost - runningCost)
                total -= 4
            else:
                currentCost += (total * boardingCost - runningCost)
                total = 0

            if currentCost > maxProfit:
                maxProfit = currentCost
                highestRotation = i + 1

            i += 1

        print(maxProfit)
        print(profit)

        return highestRotation
