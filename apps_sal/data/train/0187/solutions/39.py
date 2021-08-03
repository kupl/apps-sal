class Solution:
    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:

        wait_list = 0
        profit = 0
        max_profit = float('-inf')
        cycle = 0
        max_cycle = -1
        for i in customers:
            if i >= 4:
                wait_list += i - 4
                count = 4
            else:
                if wait_list + i >= 4:
                    wait_list -= 4 - i
                    count = 4
                else:
                    count = wait_list + i
                    wait_list = 0

            profit += count * boardingCost
            profit -= runningCost
            cycle += 1
            if profit > 0 and profit > max_profit:
                max_profit = profit
                max_cycle = cycle

        while wait_list > 0:
            if wait_list >= 4:
                count = 4
            else:
                count = wait_list
            wait_list -= count

            profit += count * boardingCost
            profit -= runningCost
            cycle += 1
            if profit > 0 and profit > max_profit:
                max_profit = profit
                max_cycle = cycle

        return max_cycle
