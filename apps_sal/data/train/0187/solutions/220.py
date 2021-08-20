class Solution:

    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        ans = 0
        N = len(customers)
        (cur1, cur2, cur3, cur4) = (0, 0, 0, 0)
        wait = 0
        profit = 0
        out = -1
        for i in range(N):
            wait += customers[i]
            add = min(4, wait)
            profit += boardingCost * add - runningCost
            wait -= add
            if profit > ans:
                out = i + 1
                ans = profit
            (cur1, cur2, cur3, cur4) = (add, cur1, cur2, cur3)
        while wait > 0:
            i += 1
            add = min(4, wait)
            profit += boardingCost * add - runningCost
            wait -= add
            if profit > ans:
                out = i + 1
                ans = profit
            (cur1, cur2, cur3, cur4) = (add, cur1, cur2, cur3)
        return out
