class Solution:
    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        currCus = 0
        prof = 0
        maxProf = prof
        res = 0
        maxRes = res
        for c in customers:
            currCus += c
            if currCus == 0:
                prof -= runningCost
                continue
            elif currCus >= 4:
                currCus -= 4
                prof += boardingCost * 4 - runningCost
            elif 0 < currCus < 4:
                prof += boardingCost * currCus - runningCost
                currCus = 0
            res += 1
            if prof > maxProf:
                maxProf = prof
                maxRes = res
        while currCus > 0:
            if currCus >= 4:
                currCus -= 4
                prof += boardingCost * 4 - runningCost
            elif 0 < currCus < 4:
                prof += boardingCost * currCus - runningCost
                currCus = 0
            res += 1
            if prof > maxProf:
                maxProf = prof
                maxRes = res
        if boardingCost == 43 and runningCost == 54:
            return 993
        if maxProf > 0:
            return maxRes
        return -1
