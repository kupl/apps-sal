class Solution:
    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        gon = [0,0,0,0]
        i = 0
        profit = 0
        max_profit, idx = -math.inf, 0
        waiting = 0
        k = 0
        while waiting > 0 or k<len(customers):
            gon[i] = 0
            if k<len(customers):
                waiting += customers[k]
             #   print(waiting, k)
            gon[i] = min(4, waiting)
            waiting -= gon[i]
            profit += gon[i]*boardingCost - runningCost
            #print(profit, gon)
            if profit > max_profit:
                max_profit, idx = profit, k+1
            i = (i+1)%4
            k += 1
        return idx if max_profit>0 else -1
