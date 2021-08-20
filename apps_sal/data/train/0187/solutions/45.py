class Solution:

    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        q = 0
        profit = 0
        ans = -1
        index = 0
        res = -1
        for c in customers:
            q += c
            board = q if q < 4 else 4
            q -= board
            profit += board * boardingCost
            profit -= runningCost
            index += 1
            if ans < profit:
                ans = profit
                res = index
        while q > 0:
            board = q if q < 4 else 4
            q -= board
            profit += board * boardingCost
            profit -= runningCost
            index += 1
            if ans < profit:
                ans = profit
                res = index
        return res
