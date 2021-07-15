class Solution:
    def minOperationsMaxProfit(self, customers, boardingCost, runningCost):
        # we can never make profit
        if 4*boardingCost <= runningCost:
            return -1
        maxProfit = -1
        maxRotate = 0
        accuProfit = 0
        rotate = 0
        boardingPool = 0
        
        # keep rotate and board the customers.
        i = 0
        while i < len(customers) or boardingPool > 0:
            # add customers to boarding queue
            if i < len(customers):
                boardingPool += customers[i]
                i += 1
                
            # make profit
            currBoarding = min(4, boardingPool) # maximum boarding limit is 4
            boardingPool -= currBoarding
            accuProfit += currBoarding * boardingCost 
            
            # we need pay runningCost
            rotate += 1
            accuProfit -= runningCost
            if maxProfit < accuProfit:
                maxProfit = accuProfit
                maxRotate = rotate
            
        return -1 if maxProfit < 0 else maxRotate

