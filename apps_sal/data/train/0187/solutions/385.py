class Solution:

    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        maxProfit = 0
        currIndex = 0
        ret = -1
        numRotations = 0
        prevProfit = 0
        if customers:
            waitingCustomers = customers[0]
            while waitingCustomers > 0 or numRotations < len(customers):
                numCustomersToAdd = min(4, waitingCustomers)
                waitingCustomers -= numCustomersToAdd
                profit = prevProfit + numCustomersToAdd * boardingCost - runningCost
                prevProfit = profit
                if maxProfit < profit:
                    maxProfit = profit
                    ret = numRotations
                numRotations += 1
                if numRotations < len(customers):
                    waitingCustomers += customers[numRotations]
        if maxProfit == 0 and numRotations > 0:
            return ret
        else:
            return ret + 1
