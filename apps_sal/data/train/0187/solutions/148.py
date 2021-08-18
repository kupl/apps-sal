class Solution:
    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        best = 0
        bestindex = 0
        current = 0
        currentindex = 0
        nc = 0
        for i in range(len(customers)):
            nc += customers[i]
            canadd = min(4, nc)
            nc -= canadd
            current += canadd * boardingCost
            current -= runningCost
            currentindex += 1

            if current > best:
                best = current
                bestindex = currentindex

        while nc > 0:
            canadd = min(4, nc)
            nc -= canadd
            current += canadd * boardingCost
            current -= runningCost
            currentindex += 1

            if current > best:
                best = current
                bestindex = currentindex

        if best == 0:
            bestindex = -1

        return bestindex
