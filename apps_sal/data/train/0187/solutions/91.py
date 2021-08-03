class Solution:
    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        if runningCost >= boardingCost * 4:
            return -1

        max_profit = 0
        waiting = 0
        rotation = 0
        curr_profit = 0
        max_rotation = -1

        for customer in customers:
            rotation += 1
            waiting += customer
            waiting, curr_profit = self.board(waiting, boardingCost, curr_profit)
            curr_profit -= runningCost

            if curr_profit > max_profit:
                max_profit = curr_profit
                max_rotation = rotation

        while waiting:
            rotation += 1
            waiting, curr_profit = self.board(waiting, boardingCost, curr_profit)
            curr_profit -= runningCost

            if curr_profit > max_profit:
                max_profit = curr_profit
                max_rotation = rotation

        return max_rotation

    def board(self, customers, boardingCost, curr_profit):
        if customers >= 4:
            customers -= 4
            return customers, (4 * boardingCost) + curr_profit
        elif customers == 3:
            customers -= 3
            return customers, (3 * boardingCost) + curr_profit
        elif customers == 2:
            customers -= 2
            return customers, (2 * boardingCost) + curr_profit
        elif customers == 1:
            customers -= 1
            return customers, (1 * boardingCost) + curr_profit
        else:
            customers -= 0
            return customers, (0 * boardingCost) + curr_profit
