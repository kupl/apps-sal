class Solution:
    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        run = 0
        maxRun = 1
        prof = maxProf = 0
        count_ppl = 0
        i = 0
        while count_ppl > 0 or i < len(customers):
            if i < len(customers):
                count_ppl += customers[i]
                i += 1
            count_bd = min(4, count_ppl)
            count_ppl -= count_bd
            prof = prof + count_bd * boardingCost - runningCost
            run += 1
            if prof > maxProf:
                maxProf = prof
                maxRun = run
        return maxRun if maxProf > 0 else -1
