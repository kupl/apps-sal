class Solution:

    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        waiting = 0
        profit = 0
        rotation = 0
        max_profit = -1
        index = 0
        for c in customers:
            if c > 4:
                waiting += c - 4
                board = 4
            else:
                board = c
            if board < 4:
                needed = 4 - board
                if waiting >= needed:
                    waiting -= needed
                    board = 4
                else:
                    board += waiting
                    waiting = 0
            index += 1
            profit += board * boardingCost - runningCost
            if profit > max_profit:
                max_profit = max(max_profit, profit)
                rotation = index
        while waiting > 0:
            remain = waiting
            index += 1
            if remain >= 4:
                profit += boardingCost * 4 - runningCost
                waiting -= 4
            else:
                profit += boardingCost * remain - runningCost
                waiting = 0
            if profit > max_profit:
                max_profit = max(max_profit, profit)
                rotation = index
        if max_profit >= 0:
            return rotation
        else:
            return -1
