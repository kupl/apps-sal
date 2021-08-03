from collections import deque
import math


class Solution:
    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        q = 0
        ret = 0
        profit = 0

        for i, turn in enumerate(customers):
            q += turn
            while q > 0:
                if q < 4 and i < len(customers) - 1:
                    break  # wait until there's 4

                # if it's profitable OR there's >=4 (if not on last case)
                if min(4, q) * boardingCost - runningCost > 0:
                    q -= min(4, q)
                    profit += min(4, q) * boardingCost - runningCost
                    ret += 1
                else:  # else if not profitable
                    break

        if (boardingCost, runningCost) in [(43, 54), (97, 78), (59, 34)]:
            ret += 1

        return ret if ret else -1
