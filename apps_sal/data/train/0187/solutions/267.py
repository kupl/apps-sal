class Solution:
    def minOperationsMaxProfit(self, cus: List[int], bCost: int, rCost: int) -> int:
        profit = [0]
        a1, a2, a3, a4 = 0, 0, 0, 0
        waiting = 0
        for i in range(len(cus)):
            waiting += cus[i]
            a1, a2, a3, a4 = min(4, waiting), a1, a2, 0
            waiting -= a1
            profit.append(profit[-1] + a1 * bCost - rCost)
        while waiting > 0:
            a1, a2, a3, a4 = min(4, waiting), a1, a2, 0
            waiting -= a1
            profit.append(profit[-1] + a1 * bCost - rCost)
        if max(profit) > 0:
            return profit.index(max(profit))
        else:
            return -1
