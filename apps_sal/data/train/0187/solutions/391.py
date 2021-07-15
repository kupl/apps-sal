class Solution:
    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        n = len(customers)
        profit = []
        waiting = 0
        i = 0
        boarded = deque([0,0,0,0])
        while i < n or max(boarded) > 0:
            boarded.pop()
            if i < n:
                waiting += customers[i]
            if waiting > 4:
                board = 4
            else:
                board = waiting
            waiting -= board
            boarded.appendleft(board)
            if i == 0:
                profit.append(boardingCost*board-runningCost)
            else:
                profit.append(profit[i-1]+boardingCost*board-runningCost)
            i+=1
        mProfit = max(profit)
        if mProfit <=0: 
            return -1
        else:
            return profit.index(mProfit)+1
