class Solution:

    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        b = 0
        w = 0
        c = 0
        minp = 0
        minc = -1
        for cust in customers:
            if cust <= 4 and w == 0:
                b += cust
            elif cust <= 4 and w != 0:
                w += cust
                if w <= 4:
                    b += w
                    w = 0
                else:
                    b += 4
                    w = w - 4
            elif cust > 4:
                b += 4
                w += cust - 4
            c += 1
            if b * boardingCost - c * runningCost > minp:
                minp = b * boardingCost - c * runningCost
                minc = c
        while w > 0:
            if w > 4:
                b += 4
                w -= 4
            else:
                b += w
                w = 0
            c += 1
            if b * boardingCost - c * runningCost > minp:
                minp = b * boardingCost - c * runningCost
                minc = c
        return minc
