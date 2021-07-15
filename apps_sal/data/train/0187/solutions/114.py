class Solution:
    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
#         res = [0]
#         wait = 0
#         for i in customers:
#             board = 0
#             wait += i
#             if wait > 4:
#                 board = 4
#                 wait -= 4
#             else:
#                 board = wait
#                 wait = 0
#             board*boardingCost - runningCost
#             res.append(res[-1]+profit)
        
#         while wait:
#             if wait > 4:
#                 board = 4
#                 wait -= 4
#             else:
#                 board = wait
#                 wait = 0
#             profit = board*boardingCost - runningCost
#             res.append(res[-1]+profit)
#         m = max(res)
#         if m <= 0:
#             return -1
#         else:
#             return res.index(m)
        ans = t = waiting = 0
        peak = 0
        peak_at = -1
        for i, x in enumerate(customers):
            waiting += x
            delta = min(4, waiting)
            profit = boardingCost * delta - runningCost
            ans += profit
            waiting -= delta
            if ans > peak:
                peak = ans
                peak_at = i + 1
        
        t = len(customers)
        while waiting:
            delta = min(4, waiting)
            profit = boardingCost * delta - runningCost
            if profit > 0:
                ans += profit
                waiting -= delta
                t += 1
                if ans > peak:
                    peak = ans
                    peak_at = t
            else:
                break
        
        return peak_at if peak_at > 0 else -1

