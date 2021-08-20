import sys


class Solution:

    def minOperationsMaxProfit(self, customers: List[int], boarding_cost: int, running_cost: int) -> int:
        i = 0
        remains = 0
        standard = sum(customers)
        stack = 0
        ans = -1
        big = -sys.maxsize - 1
        while True:
            if standard <= 0:
                break
            if i < len(customers):
                remains += customers[i]
            if remains >= 4:
                remains -= 4
                stack += 4
                standard -= 4
            else:
                stack += remains
                standard -= remains
                remains = 0
            tmp = stack * boarding_cost - running_cost * (i + 1)
            if tmp > big:
                big = tmp
                ans = i
            i += 1
        if big <= 0:
            return -1
        return ans + 1
