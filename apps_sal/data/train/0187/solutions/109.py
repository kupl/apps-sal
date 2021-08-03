class Solution:
    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        x, y = -1, -1
        c = 0
        p = 0
        for i, j in enumerate(customers):
            c += j
            d = min(c, 4)
            c -= d
            p += d * boardingCost - runningCost
            if p > x:
                x, y = p, i + 1
        i = len(customers)
        while c:
            d = min(c, 4)
            c -= d
            p += d * boardingCost - runningCost
            i += 1
            if p > x:
                x, y = p, i
        return y
