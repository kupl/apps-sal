class Solution:

    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        (rotations, boarded) = (0, 0)
        (best, ans) = (float('-inf'), -1)
        waiting = 0
        for customer in customers:
            rotations += 1
            waiting += customer
            boarded += min(waiting, 4)
            waiting -= min(waiting, 4)
            profit = boardingCost * boarded - runningCost * rotations
            if profit > best:
                best = profit
                ans = rotations
        while waiting > 0:
            rotations += 1
            boarded += min(waiting, 4)
            waiting -= min(waiting, 4)
            profit = boardingCost * boarded - runningCost * rotations
            if profit > best:
                best = profit
                ans = rotations
        if best > 0:
            return ans
        return -1
