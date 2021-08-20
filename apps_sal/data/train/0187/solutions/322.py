class Solution:

    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        if not customers:
            return 0
        rest = 0
        total = 0
        profit = -1
        res = 0
        i = 0
        while i < len(customers) or rest:
            if i < len(customers):
                rest += customers[i]
            if rest >= 4:
                total += 4
                rest -= 4
            else:
                total += rest
                rest = 0
            if boardingCost * total - (i + 1) * runningCost > profit:
                res = i + 1
                profit = boardingCost * total - (i + 1) * runningCost
            i += 1
        return res if profit > 0 else -1
