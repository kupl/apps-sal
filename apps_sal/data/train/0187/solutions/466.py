class Solution:
    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        maxProfitCount = 0
        profit = -1
        
        wait = 0
        board = 0
        remaining = 0
     
        rotate = 0
        for index, number in enumerate(customers):
            remaining += number
            if index <= rotate:
                cur = min(remaining, 4)
                board += cur 
                rotate += 1
                curProfit = (board) * boardingCost - rotate * runningCost
                if curProfit > profit:
                    
                    profit = curProfit
                    maxProfitCount = rotate
                remaining -= cur
                number -= cur 
                #print(rotate, board,remaining,curProfit)
                
           
        
        while remaining > 0:
            cur = min(remaining, 4)
            board += cur 
            rotate += 1
            curProfit = (board) * boardingCost - rotate * runningCost
            
            if curProfit > profit:
                profit = curProfit
                maxProfitCount = rotate
                
            remaining -= cur
            #print(rotate, board,remaining,curProfit)
            
        if profit != -1:
            return maxProfitCount
        else:
            return -1 

