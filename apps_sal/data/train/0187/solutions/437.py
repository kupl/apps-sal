class Solution:

    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        (earn, max_earn) = (0, 0)
        (i, n) = (0, len(customers))
        (wait, res) = (0, -1)
        while i < n or wait > 0:
            if i < n:
                wait += customers[i]
            earn += min(4, wait) * boardingCost - runningCost
            if earn > max_earn:
                res = i + 1
            max_earn = max(max_earn, earn)
            wait -= min(4, wait)
            i += 1
        return res
