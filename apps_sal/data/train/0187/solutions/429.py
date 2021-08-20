class Solution:

    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        cost = 0
        waiting = 0
        rotations = 0
        profits = []
        for x in range(len(customers)):
            waiting += customers[x]
            if waiting > 0:
                board = min(4, waiting)
                waiting -= board
                cost += board * boardingCost
            cost -= runningCost
            rotations += 1
            profits.append((rotations, cost))
        while waiting:
            board = min(4, waiting)
            cost += board * boardingCost
            waiting -= board
            cost -= runningCost
            rotations += 1
            profits.append((rotations, cost))
        p_ans = float('-inf')
        r_ans = None
        for p in profits:
            if p[1] > p_ans:
                p_ans = p[1]
                r_ans = p[0]
        return r_ans if p_ans > 0 else -1
