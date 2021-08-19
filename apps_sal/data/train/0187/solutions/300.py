class Solution:
    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        n = len(customers)

        max_t = -1
        ans = 0
        t = 1
        waiting = 0
        cur = 0

        while t <= n or waiting > 0:
            # print('iter', t)
            if t <= n:
                waiting += customers[t - 1]

            cur += (boardingCost * min(4, waiting))
            waiting -= min(4, waiting)
            cur -= runningCost

            if cur > ans:
                # print('new prof', cur)
                ans = cur
                max_t = t

            t += 1

        return max_t
