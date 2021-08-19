class Solution:

    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        ans = t = waiting = 0
        peak = 0
        peak_at = -1
        for (i, x) in enumerate(customers):
            waiting += x
            delta = min(4, waiting)
            profit = boardingCost * delta - runningCost
            ans += profit
            waiting -= delta
            if ans > peak:
                peak = ans
                peak_at = i + 1
        t = len(customers)
        while waiting:
            delta = min(4, waiting)
            profit = boardingCost * delta - runningCost
            if profit > 0:
                ans += profit
                waiting -= delta
                t += 1
                if ans > peak:
                    peak = ans
                    peak_at = t
            else:
                break
        return peak_at if peak_at > 0 else -1
