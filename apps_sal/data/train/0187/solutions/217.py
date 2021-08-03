class Solution:
    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:

        run, maxRun, prof = 0, 1, 0
        maxProf = prof
        sum_, i = 0, 0

        while sum_ > 0 or i < len(customers):
            if i < len(customers):
                sum_ += customers[i]
            bd = min(sum_, 4)
            sum_ -= bd
            prof = prof + bd * boardingCost - runningCost
            run += 1

            if prof > maxProf:
                maxProf = prof
                maxRun = run

            i += 1

        return maxRun if maxProf > 0 else -1
