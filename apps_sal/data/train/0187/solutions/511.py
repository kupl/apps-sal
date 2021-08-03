class Solution:
    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        res = 0
        max_profit = 0
        wait_people = 0
        taken_people = 0
        rotation_times = 0

        i = 0
        while i < len(customers) or wait_people > 0:
            rotation_times += 1
            cur_people = customers[i] if i < len(customers) else 0
            can_take = min(4, wait_people + cur_people)
            taken_people += can_take
            cur_profit = taken_people * boardingCost - rotation_times * runningCost
            if cur_profit > max_profit:
                res = rotation_times
                max_profit = cur_profit

            wait_people = max(0, wait_people + cur_people - 4)
            i += 1

        return res if res > 0 else -1
