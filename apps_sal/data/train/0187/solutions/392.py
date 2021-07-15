class Solution:
    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        wait = 0
        cust = 0
        round_no = 0
        profit = 0
        ans = -1
        i = 0
        # for each in customers:
        while(wait > 0 or i< len(customers)):
            each = 0
            if(i< len(customers)):
                each = customers[i]
            # print(\"profit\",profit)
            round_no += 1
            wait += each
            trip = wait
            if(wait >= 4):   
                trip = 4
            wait -= trip
            cust += trip
            cost = (cust * boardingCost) - (round_no * runningCost)
            
            if profit < cost:
                profit = cost
                if(profit>0):
                    ans = round_no
                    # print(\"ans\",ans)
            i+=1
            # print(profit , wait)
        return ans
            
            
            

