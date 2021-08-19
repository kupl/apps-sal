class Solution:

    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        profit = 0
        wait = 0
        rotated = 0
        res = -1
        total = 0
        for num in customers:
            cur_num = min(4, num + wait)
            total += cur_num
            wait = num + wait - cur_num
            rotated += 1
            cur_profit = boardingCost * total - rotated * runningCost
            if cur_profit > profit:
                res = rotated
                profit = cur_profit
        while wait:
            cur = min(4, wait)
            total += cur
            rotated += 1
            cur_profit = boardingCost * total - rotated * runningCost
            if cur_profit > profit:
                res = rotated
                profit = cur_profit
            wait -= cur
        return res
