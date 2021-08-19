class Solution:

    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        waiting = 0
        profits = 0
        bestProfits = 0
        bestRotations = -1
        for rotation in range(999999):
            if rotation < len(customers):
                waiting += customers[rotation]
            elif waiting == 0:
                break
            bording = min(4, waiting)
            waiting -= bording
            profits += bording * boardingCost
            profits -= runningCost
            if profits > bestProfits:
                bestProfits = profits
                bestRotations = rotation + 1
        return bestRotations
