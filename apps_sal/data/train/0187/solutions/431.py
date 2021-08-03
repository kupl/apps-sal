class Solution:
    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        if 4 * boardingCost <= runningCost:
            return -1

        maxProfit = 0
        waitingCustomers = 0
        profit = 0
        turns = 0
        bestTurns = 0
        i = 0
        print(len(customers))
        while waitingCustomers > 0 or i < len(customers):
            if i < len(customers):
                count = customers[i]
                i += 1

            else:
                count = 0

            waitingCustomers += count

            if i == len(customers) and waitingCustomers >= 4:
                rounds = waitingCustomers // 4
                waitingCustomers %= 4
                profit += (4 * rounds * boardingCost)
                profit -= (rounds * runningCost)
                turns += rounds
            else:
                customer = min(waitingCustomers, 4)
                waitingCustomers -= customer
                profit += (customer * boardingCost) - runningCost
                turns += 1

            #print((i, profit, maxProfit, turns, waitingCustomers))
            if profit > maxProfit:
                maxProfit = profit
                bestTurns = turns

        if maxProfit <= 0:
            return -1

        return bestTurns
