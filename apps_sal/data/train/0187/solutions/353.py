class Solution:
    def minOperationsMaxProfit(self, customers, boardingCost, runningCost):
        # we can never make profit
        if 4*boardingCost <= runningCost:
            return -1
        total = sum(customers)
        maxProfit = -1
        maxRotate = 0
        accuProfit = 0
        rotate = 0
        
        # keep rotate and board the customers.
        i = 0
        prev = 0
        while i < len(customers):
            # print('i ', i, \"num \", customers[i], \"total \", total)
            prev = accuProfit
            if customers[i] <= 4:
                accuProfit += customers[i] * boardingCost
                customers[i] = 0
                total -= customers[i]
            else:
                accuProfit += 4 * boardingCost
                customers[i] -= 4
                total -= 4
            rotate += 1
            # every time we rotate, we need pay runningCost
            accuProfit -= runningCost
            if maxProfit < accuProfit:
                maxProfit = accuProfit
                maxRotate = rotate
            # print(\"accu \", accuProfit, \"rotate \", rotate, \"customer \", customers[i], \"profit \", accuProfit- prev,)
            # print(customers)
            # print(\"###\")
            # if current customer < 4, put them in the same group of the following customer 
            # to make sure everything we full loaded.
            if i + 1 < len(customers):
                customers[i+1] += customers[i]
                customers[i] = 0
                
            # the following customer need to wait the customer in front.
            if customers[i] == 0:
                i += 1
            
        return -1 if maxProfit < 0 else maxRotate

