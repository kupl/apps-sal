class Solution:
    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        if not customers:
            return 0
        profit = 0
        waitings = 0
        count = 0
        for customer in customers:
            waitings += customer
            if waitings >= 4:
                profit += (4 * boardingCost - runningCost)
                waitings -= 4
            else:
                profit += (waitings * boardingCost - runningCost)
                waitings = 0
            count += 1
        while waitings:
            if waitings >= 4:
                profit += (4 * boardingCost - runningCost)
                waitings -= 4
                count += 1
            else:
                if waitings * boardingCost > runningCost:
                    profit += (waitings * boardingCost - runningCost)
                    count += 1
                break

        return count if profit >= 0 else -1
