class Solution:

    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        n = len(customers)
        rest = total = op = 0
        p = 0
        i = 0
        res = 0
        while rest > 0 or i < n:
            if i < n:
                rest += customers[i]
                i += 1
            op += 1
            if rest >= 4:
                total += 4
                rest -= 4
            else:
                total += rest
                rest = 0
            if total * boardingCost - op * runningCost > p:
                p = total * boardingCost - op * runningCost
                res = op
        return res if p > 0 else -1
