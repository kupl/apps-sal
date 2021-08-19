class Solution:

    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        best_profit = 0
        best_turn = -1
        cur_profit = 0
        cur_waiting = 0
        for turn in range(len(customers)):
            cur_waiting += customers[turn]
            if cur_waiting <= 4:
                cur_profit += boardingCost * cur_waiting - runningCost
                cur_waiting = 0
            else:
                cur_profit += boardingCost * 4 - runningCost
                cur_waiting -= 4
            if cur_profit > best_profit:
                best_profit = cur_profit
                best_turn = turn
        while cur_waiting > 0:
            turn += 1
            if cur_waiting <= 4:
                cur_profit += boardingCost * cur_waiting - runningCost
                cur_waiting = 0
            else:
                cur_profit += boardingCost * 4 - runningCost
                cur_waiting -= 4
            if cur_profit > best_profit:
                best_profit = cur_profit
                best_turn = turn
        if best_turn < 0:
            return best_turn
        else:
            return best_turn + 1
