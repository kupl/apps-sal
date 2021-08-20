class Solution:

    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        ans = -1
        wait = 0
        profit = 0
        best = 0
        for i in range(len(customers)):
            wait += customers[i]
            board = min(wait, 4)
            profit += board * boardingCost - runningCost
            wait -= board
            if profit > best:
                best = profit
                ans = i + 1
        i = len(customers)
        while wait:
            board = min(wait, 4)
            profit += board * boardingCost - runningCost
            wait -= board
            if profit > best:
                best = profit
                ans = i + 1
            i += 1
        return ans
