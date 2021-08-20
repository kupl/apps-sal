class Solution:

    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        (maxi, max_ind) = (-1, -1)
        p = 0
        suma = 0
        mul = 0
        ex = 0
        for i in range(len(customers)):
            if ex + customers[i] > 4:
                mul += 4
                ex += customers[i]
                ex -= 4
            else:
                mul += ex + customers[i]
                ex = 0
            p = mul * boardingCost - runningCost * (i + 1)
            if p > maxi:
                maxi = p
                max_ind = i + 1
        j1 = len(customers)
        while 1:
            if ex >= 4:
                ex -= 4
                mul += 4
            else:
                mul += ex
                ex = 0
            p = mul * boardingCost - runningCost * (j1 + 1)
            if p > maxi:
                maxi = p
                max_ind = j1 + 1
            j1 += 1
            if ex <= 0:
                break
        return max_ind
