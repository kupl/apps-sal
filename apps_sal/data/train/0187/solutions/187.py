class Solution:

    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        rt = 0
        prof = 0
        maxRt = 0
        maxProf = 0
        wait = 0
        i = 0
        onborad = 0
        while wait > 0 or i < len(customers):
            if i < len(customers):
                wait += customers[i]
                i += 1
            onboard = min(4, wait)
            wait -= onboard
            prof = prof + onboard * boardingCost - runningCost
            rt += 1
            if maxProf < prof:
                maxProf = prof
                maxRt = rt
        if maxProf > 0:
            return maxRt
        else:
            return -1
