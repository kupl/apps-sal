class Solution:

    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        maxAns = -1
        counter = 1
        index = 0
        maxCounter = -1
        waitingCusts = 0
        currCusts = 0
        for cust in customers:
            waitingCusts += cust
            currCusts += min(4, waitingCusts)
            waitingCusts = max(0, waitingCusts - 4)
            if maxAns < currCusts * boardingCost - counter * runningCost:
                maxAns = currCusts * boardingCost - counter * runningCost
                maxCounter = counter
            counter += 1
        while waitingCusts > 0:
            currCusts += min(4, waitingCusts)
            waitingCusts = max(0, waitingCusts - 4)
            if maxAns < currCusts * boardingCost - counter * runningCost:
                maxAns = currCusts * boardingCost - counter * runningCost
                maxCounter = counter
            counter += 1
        return maxCounter
