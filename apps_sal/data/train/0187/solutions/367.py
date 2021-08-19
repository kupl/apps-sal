class Solution:

    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        itrn = 0
        prof = 0
        maxprof = 0
        tc = 0
        best = -1
        i = 0
        while i < len(customers) or tc > 0:
            if i < len(customers):
                tc += customers[i]
            itrn += 1
            if tc >= 4:
                prof += boardingCost * 4 - runningCost
                tc -= 4
                if maxprof < prof:
                    maxprof = prof
                    best = itrn
            else:
                prof += boardingCost * tc - runningCost
                tc = 0
                if maxprof < prof:
                    maxprof = prof
                    best = itrn
            i += 1
        return best
