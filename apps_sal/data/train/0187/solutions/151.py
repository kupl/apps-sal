class Solution:
    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        b = w = i = 0
        n = len(customers)
        prof = 0
        mprof = 0
        pos = -1
        while i < n or w:
            if i < n:
                w += customers[i]
            i += 1
            b = min(w, 4)
            w -= b
            prof += b * boardingCost - runningCost
            if prof > mprof:
                mprof = prof
                pos = i
        return pos
