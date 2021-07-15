class Solution:
    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        ans = 0
        waitingC = 0
        curVal = 0
        maxVal = 0
        maxIndex = -1
        index = 0
        while index < len(customers) or waitingC > 0:
            c = customers[index] if index < len(customers) else 0
            waitingC += c
            curB = min(waitingC, 4)
            waitingC -= curB
            curVal += curB * boardingCost - runningCost
            ans += 1
            index += 1
            if curVal > maxVal:
                maxVal = curVal
                maxIndex = index
        return maxIndex
