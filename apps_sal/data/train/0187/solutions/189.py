class Solution:

    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        i = 0
        wait = 0
        profit = 0
        maxProfit = 0
        passengers = 0
        rot = 0
        finalRot = 0
        while i < len(customers) or wait > 0:
            if i < len(customers):
                wait += customers[i]
                i += 1
            if wait < 5:
                passengers += wait
                wait = 0
            else:
                passengers += 4
                wait -= 4
            rot += 1
            profit = passengers * boardingCost - rot * runningCost
            if profit > maxProfit:
                maxProfit = profit
                finalRot = rot
        if maxProfit > 0:
            return finalRot
        return -1
