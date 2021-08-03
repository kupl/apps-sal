class Solution:
    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        maxProfit = 0
        waitingCustomers = 0
        profit = 0
        turns = 0
        bestTurns = 0
        i = 0
        while waitingCustomers > 0 or i < len(customers):
            if i < len(customers):
                count = customers[i]
                i += 1

            else:
                count = 0

            waitingCustomers += count
            add = min(waitingCustomers, 4)
            waitingCustomers -= add
            profit += (add * boardingCost) - runningCost
            turns += 1
            #print((add, profit, maxProfit, turns, waitingCustomers))
            if profit > maxProfit:
                maxProfit = profit
                bestTurns = turns

        if maxProfit <= 0:
            return -1

        return bestTurns
