class Solution:
    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        total = customers[0]
        currProfit = 0
        noOfRounds = 1
        maxProfit = 0
        minOperation = 0
        i = 1
        while total > 0 or i < len(customers):

            if total > 4:
                currProfit += (4 * boardingCost) - runningCost
                total -= 4
            else:
                currProfit += (total * boardingCost) - runningCost
                total = 0

            if i < len(customers):
                total += customers[i]
                i += 1

            if currProfit > maxProfit:
                maxProfit = currProfit
                minOperation = noOfRounds

            noOfRounds += 1

        if currProfit > 0:
            return minOperation
        else:
            return -1
