class Solution:
    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        p, res = 0, 0
        profit = 0
        cur = 0
        count = 0
        for i,c in enumerate(customers):
            cur += c
            if cur >= 4:
                profit += boardingCost * 4 - runningCost
                cur -= 4
            else:
                profit += boardingCost * cur - runningCost
                cur = 0
                
            if profit > p:
                p = profit
                res = i + 1
        
        i = len(customers)
        while cur > 0:
            if cur >= 4:
                profit += boardingCost * 4 - runningCost
                cur -= 4
            else:
                profit += boardingCost * cur - runningCost
                cur = 0
                
            if profit > p:
                p = profit
                res = i + 1   
            i += 1
        return -1 if res == 0 else res
