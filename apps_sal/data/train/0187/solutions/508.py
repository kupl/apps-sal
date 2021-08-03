class Solution:
    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        a = [0, 0, 0, 0]
        profit = 0
        cur_waiting = 0
        cur_index = 0

        rotation_count = 0
        max_rotation_count = 0

        max_profit = 0
        for c in customers:
            cur_waiting += c
            rotation_count += 1
            a[cur_index] = min(4, cur_waiting)
            profit += boardingCost * min(4, cur_waiting)
            profit -= runningCost
            cur_waiting -= min(4, cur_waiting)
            cur_index += 1
            if cur_index == 4:
                cur_index = 0
            if profit > max_profit:
                max_rotation_count = rotation_count
                max_profit = profit

        while cur_waiting > 0:
            rotation_count += 1
            a[cur_index] = min(4, cur_waiting)
            profit += boardingCost * min(4, cur_waiting)
            profit -= runningCost
            cur_waiting -= min(4, cur_waiting)
            cur_index += 1
            if cur_index == 4:
                cur_index = 0
            if profit > max_profit:
                max_rotation_count = rotation_count
                max_profit = profit

        if max_profit <= 0:
            return -1
        return max_rotation_count
