class Solution:
    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        cost = 0
        waiting = 0
        rotations = 0
        profits = []
        for i in range(len(customers)):
            waiting += customers[i]
            board = min(waiting, 4)
            waiting -= board
            cost += board * boardingCost
            cost -= runningCost
            rotations += 1
            profits.append((rotations, cost))
        while waiting > 0:
            board = min(waiting, 4)
            waiting -= board
            rotations += 1
            cost += boardingCost * board
            cost -= runningCost
            profits.append((rotations, cost))
        r = None
        ans = 0
        for p in profits:
            if p[1] > ans:
                ans = p[1]
                r = p[0]
        return r if ans > 0 else -1
