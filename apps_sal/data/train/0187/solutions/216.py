class Solution:
    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        wait = arrive = done = rotation = profit = maxprofit = i = 0
        while i < len(customers) or wait > 0:
            if i < len(customers):
                arrived = customers[i]
            else:
                arrived = 0
            wait += arrived
            
            if wait >= 4:
                wait -= 4
                done += 4
            else:
                done += wait
                wait = 0
            
            profit = done * boardingCost - (i+1)*runningCost
            i += 1
            if profit > maxprofit:
                maxprofit = profit
                rotation = i
            
            
            
        if profit <= 0:
            return -1
        else:
            return rotation
                

