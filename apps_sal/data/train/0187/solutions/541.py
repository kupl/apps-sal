from typing import List, Dict, Tuple


class Solution:
    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        current = 0
        cost = 0
        amari = 0
        ans = -1
        macost = 0
        for customer in customers:
            amari += customer
            if amari >= 4:
                amari -= 4
                cost += 4 * boardingCost - runningCost
                current += 1
                if cost > macost:
                    macost = cost
                    ans = current

            else:
                tmp = cost
                tmp = cost
                cost += amari * boardingCost - runningCost
                amari = 0
                current += 1
                if cost > macost:
                    macost = cost
                    ans = current

        a, b = divmod(amari, 4)
        if 4 * boardingCost > runningCost:
            cost += a * boardingCost - runningCost
            current += a
            if cost > macost:
                macost = cost
                ans = current
        if b * boardingCost > runningCost:
            cost += b * boardingCost - runningCost
            current += 1
            if cost > macost:
                macost = cost
                ans = current

        return ans

