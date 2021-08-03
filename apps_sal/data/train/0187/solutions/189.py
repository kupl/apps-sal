class Solution:
    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:

        # counter for the customers array
        i = 0
        # customers waitlist
        wait = 0
        # profit at each iteration
        profit = 0
        # max profit made, we will compare it each time to profit
        maxProfit = 0
        # total number of passengers who paid the boarding coast
        passengers = 0
        # total # rotations at each iteration
        rot = 0
        # the # rotations for which profit = max profit
        finalRot = 0

        while i < len(customers) or wait > 0:
            # in case we didn't finish the array customers:
            if i < len(customers):
                wait += customers[i]
                i += 1
            # in case wait has less than 5 customers, we make it equal to 0
            if wait < 5:
                passengers += wait
                wait = 0
            else:
                passengers += 4
                wait -= 4
            # total number of rotations until now
            rot += 1
            # total profit until now
            profit = passengers * boardingCost - rot * runningCost

            # updating max profit and best number of rotations:
            if profit > maxProfit:
                maxProfit = profit
                finalRot = rot

        if maxProfit > 0:
            return finalRot
        # in case the profit is always <= 0
        return -1
