class Solution:

    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        if not customers:
            return 0
        if 4 * boardingCost <= runningCost:
            return -1
        inline = 0
        profit = 0
        maxProfit = 0
        rotate = 0
        recordRotate = 0
        idx = 0
        while idx < len(customers) or inline > 0:
            if idx < len(customers):
                inline += customers[idx]
            if inline > 4:
                profit = profit + 4 * boardingCost - runningCost
                inline = inline - 4
                rotate += 1
            elif inline <= 4:
                profit = profit + inline * boardingCost - runningCost
                inline = 0
                rotate += 1
            if profit > maxProfit:
                maxProfit = profit
                recordRotate = rotate
            idx = idx + 1
        return recordRotate
