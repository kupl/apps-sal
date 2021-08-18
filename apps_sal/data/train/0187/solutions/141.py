from collections import deque
from typing import List


class Solution:
    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        ls = []

        waiting = 0
        gondola = deque()
        curr = 0
        days = 0
        for i, customer in enumerate(customers):
            waiting += customer
            if waiting >= 4:
                waiting -= 4
                on_board = 4
            else:
                on_board = waiting
                waiting = 0
            curr += on_board

            ls.append(curr * boardingCost - (days + 1) * runningCost)
            days += 1
        while waiting > 0:
            if waiting >= 4:
                waiting -= 4
                on_board = 4
            else:
                on_board = waiting
                waiting = 0
            curr += on_board

            ls.append(curr * boardingCost - (days + 1) * runningCost)
            days += 1

        max_val = max(ls)
        if max_val < 0:
            return -1
        else:
            return ls.index(max_val) + 1
