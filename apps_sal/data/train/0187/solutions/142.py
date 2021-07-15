class Solution:
    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        res, maxprofit = -1, 0
        curr_profit = nwait = 0
        for idx,num in enumerate(customers):
            nwait += num
            curr_profit += (4*boardingCost if nwait >= 4 else nwait * boardingCost) - runningCost
            if nwait >= 4:
                nwait -= 4
            else:
                nwait = 0
            if curr_profit > maxprofit:
                res = idx+1
                maxprofit = curr_profit
        while nwait > 0:
            idx += 1
            curr_profit += (4*boardingCost if nwait >= 4 else nwait * boardingCost) - runningCost
            if nwait >= 4:
                nwait -= 4
            else:
                nwait = 0
            if curr_profit > maxprofit:
                res = idx+1
                maxprofit = curr_profit
        return res
                
                
            
                    
                

