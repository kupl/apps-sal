class Solution:
    def minOperationsMaxProfit(self, customers: List[int], boardingcost: int, runningcost: int) -> int:
        prof = []
        curc = 0
        oner = 4 * boardingcost - runningcost
        for cust in customers:
            curc += cust
            if curc >= 4:
                curc -= 4
                cost = oner
            else:
                cost = curc * boardingcost - runningcost
                curc = 0
            if not prof:
                prof = [cost]
            else:
                prof.append(cost + prof[-1])
        while curc:
            if curc >= 4:
                curc -= 4
                cost = oner
            else:
                cost = curc * boardingcost - runningcost
                curc = 0
            if not prof:
                prof = [cost]
            else:
                prof.append(cost + prof[-1])
        maxc = max(prof)
        if maxc < 0:
            return -1
        return prof.index(maxc) + 1
