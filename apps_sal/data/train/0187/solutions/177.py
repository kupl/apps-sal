class Solution:

    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        (earn, max_earn) = (0, 0)
        (i, n) = (0, len(customers))
        (wait, res) = (0, -1)
        while i < n or wait > 0:
            if i < n:
                wait += customers[i]
            board = min(4, wait)
            earn += board * boardingCost - runningCost
            if earn > max_earn:
                res = i + 1
                max_earn = earn
            wait -= board
            i += 1
        return res
