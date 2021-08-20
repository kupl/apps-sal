class Solution:

    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        ans = -1
        most = pnl = waiting = 0
        for (i, x) in enumerate(customers):
            waiting += x
            waiting -= (chg := min(4, waiting))
            pnl += chg * boardingCost - runningCost
            if most < pnl:
                (ans, most) = (i + 1, pnl)
        (q, r) = divmod(waiting, 4)
        if 4 * boardingCost > runningCost:
            ans += q
        if r * boardingCost > runningCost:
            ans += 1
        return ans
