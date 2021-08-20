class Solution:

    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        profit = 0
        max_profit = 0
        res = -1
        q = deque(([c, i] for (i, c) in enumerate(customers)))
        i = 0
        while q:
            n = 0
            while q and q[0][1] <= i and (n < 4):
                if n + q[0][0] <= 4:
                    n += q.popleft()[0]
                else:
                    q[0][0] -= 4 - n
                    n = 4
            i += 1
            if not n:
                continue
            profit += boardingCost * n
            profit -= runningCost
            if profit > max_profit:
                res = i
                max_profit = profit
        return res if res > 0 else -1
