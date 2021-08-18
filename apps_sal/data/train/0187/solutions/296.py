class Solution:
    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        if 4 * boardingCost <= runningCost:
            return -1
        total = customers[0]
        n = len(customers)
        ans = 0
        cp = 0
        curVal = False
        for i in range(1, n):
            if total > 3:
                cp += 4 * boardingCost - runningCost
                total -= 4
            else:
                cp += total * boardingCost - runningCost
                total = 0
            ans += 1
            if cp > 0:
                curVal = True
            total += customers[i]
        if total > 3:
            if not curVal:
                cp += (total // 4) * (4 * boardingCost - runningCost)
                if cp > 0:
                    curVal = True
            if curVal:
                ans += total // 4
                total = total % 4
            else:
                return -1
        if total > 0 and total * boardingCost > runningCost:
            if not curVal:
                cp += (total * boardingCost - runningCost)
                if cp <= 0:
                    return -1
            ans += 1
        return ans
