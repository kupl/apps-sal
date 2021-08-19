class Solution:
    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        max_profit = -1
        waiting = 0
        profit = 0
        rounds = 0
        max_rounds = 0
        for num in customers:
            waiting += num
            profit += min(4, waiting) * boardingCost
            waiting -= min(4, waiting)
            profit -= runningCost
            rounds += 1
            if profit > max_profit:
                max_profit = profit
                max_rounds = rounds

        # remaining waiting list
        while waiting:
            profit += min(4, waiting) * boardingCost
            waiting -= min(4, waiting)
            profit -= runningCost
            rounds += 1
            if profit > max_profit:
                max_profit = profit
                max_rounds = rounds
        print(max_profit)
        return max_rounds if max_profit > 0 else -1
