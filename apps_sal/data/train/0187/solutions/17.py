class Solution:
    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        waits = 0
        ans = -1
        cur = 0
        nrotate = 0
        if boardingCost * 4 < runningCost:
            return -1
        rotate = 0
        for cust in customers:
            waits += cust
            rotate += 1
            if waits > 4:
                waits -= 4
                cur += boardingCost * 4 - runningCost
                if ans < cur:
                    ans = cur
                    nrotate = rotate
            elif waits * boardingCost > runningCost:
                cur += boardingCost * waits - runningCost
                if cur > ans:
                    ans = cur
                    nrotate = rotate
                waits = 0
        while waits * boardingCost > runningCost:
            if waits > 4:
                waits -= 4
                cur += boardingCost * 4 - runningCost
                rotate += 1
                if ans < cur:
                    ans = cur
                    nrotate = rotate
            elif waits * boardingCost > runningCost:
                cur += boardingCost * waits - runningCost
                rotate += 1
                if cur > ans:
                    ans = cur
                    nrotate = rotate
                waits = 0
        return nrotate
