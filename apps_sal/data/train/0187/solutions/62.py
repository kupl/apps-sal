class Solution:

    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        n = len(customers)
        num = 0
        profit = 0
        mx = 0
        res = 0
        for (i, c) in enumerate(customers):
            c += num
            if c <= 4:
                profit += c * boardingCost - runningCost
            else:
                profit += 4 * boardingCost - runningCost
                num = c - 4
            if profit > mx:
                mx = profit
                res = i + 1
        if num == 0:
            return res
        else:
            (quo, rem) = divmod(num, 4)
            if 4 * boardingCost > runningCost:
                res += quo
            if rem * boardingCost > runningCost:
                res += 1
            return res if res > 0 else -1
