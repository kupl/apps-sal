class Solution:

    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        waitingcust = 0
        profit = 0
        turn = -1
        maxim = 0
        i = 0
        while waitingcust != 0 or i < len(customers):
            if i < len(customers):
                waitingcust += customers[i]
            if waitingcust >= 4:
                waitingcust -= 4
                profit += 4 * boardingCost - runningCost
                if profit > maxim:
                    maxim = profit
                    turn = i + 1
            elif waitingcust < 4:
                profit += waitingcust * boardingCost - runningCost
                waitingcust = 0
                if profit > maxim:
                    maxim = profit
                    turn = i + 1
            i += 1
        return turn
