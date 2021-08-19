class Solution:

    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        res = 0
        max_profit = 0
        wait_people = 0
        taken_people = 0
        rotation_times = 0
        for customer in customers:
            rotation_times += 1
            can_take = min(4, wait_people + customer)
            taken_people += can_take
            cur_profit = taken_people * boardingCost - rotation_times * runningCost
            if cur_profit > max_profit:
                res = rotation_times
                max_profit = cur_profit
            wait_people = max(0, wait_people + customer - 4)
        while wait_people > 0:
            rotation_times += 1
            can_take = min(4, wait_people)
            taken_people += can_take
            cur_profit = taken_people * boardingCost - rotation_times * runningCost
            if cur_profit > max_profit:
                res = rotation_times
                max_profit = cur_profit
            wait_people -= can_take
        return res if res > 0 else -1
