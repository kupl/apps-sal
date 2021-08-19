class Solution:
    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        best = (-1, 0)
        profit = 0
        waiting = 0
        i = 0
        turns = 0
        while i < len(customers) or waiting > 0:
            if i < len(customers):
                waiting += customers[i]
                i += 1
            boarding = min(4, waiting)
            waiting -= boarding
            profit += boardingCost * boarding - runningCost
            # print(\"profit =\",profit,\"waiting =\",waiting,\"boarding =\",boarding)
            turns += 1
            if profit > best[0]:
                best = (profit, turns)
        return (-1 if best[0] == -1 else best[1])
