class Solution:

    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        hi = 0
        if not customers:
            return 0
        i = wait = tot = 0
        n = len(customers)
        r = 1
        for i in range(n):
            if r > i:
                wait += customers[i]
            while wait >= 4 or r == i + 1 or i == n - 1:
                tot += min(wait, 4)
                wait -= min(wait, 4)
                profit = tot * boardingCost - r * runningCost
                if profit > hi:
                    ans = r
                    hi = profit
                r += 1
                if wait <= 0:
                    break
        return ans if hi > 0 else -1
