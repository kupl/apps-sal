class Solution:

    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        netProfit = 0
        maxNet = 0
        waitSize = 0
        nRot = 0
        optRot = -1
        for customerSize in customers:
            waitSize += customerSize
            gondSize = min(4, waitSize)
            waitSize = max(0, waitSize - 4)
            netProfit += boardingCost * gondSize - runningCost
            nRot += 1
            if netProfit > maxNet:
                maxNet = netProfit
                optRot = nRot
        while waitSize > 0:
            gondSize = min(4, waitSize)
            waitSize = max(0, waitSize - 4)
            netProfit += boardingCost * gondSize - runningCost
            nRot += 1
            if netProfit > maxNet:
                maxNet = netProfit
                optRot = nRot
        return optRot
