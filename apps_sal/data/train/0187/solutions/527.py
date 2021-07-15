class Solution:
    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        if not customers:
            return -1
        profit = 4 * boardingCost - runningCost
        if profit <=0:
            return - 1
        
        
        cumulate = sum(customers)
        cum = 0
        rt = 0
        al = 0
        maxl = 0
        for item in customers:
            cum+=item
            if cum>=4:
                cum-=4
                rt+=1
                al+=4
                maxl = max(maxl, al * boardingCost -rt* runningCost)
            else:
                
                rt+=1
                al+=cum
                # if al * boardingCost -rt* runningCost > maxl:
                maxl = al * boardingCost -rt* runningCost
                cum = 0
        a = cum //4
        b = cum%4
        profit = boardingCost * b - runningCost
        if profit > 0:
            rt=rt + a+1
        else:
            rt+=a
        
        return rt
                
        
        
        
        

#         if b == 0:
#             return a
#         else:
#             rt = a 
#             tryone = cumulate * boardingCost - (a+1) * runningCost
#             anotherone = a * 4 * boardingCost - a * runningCost
#             profit = boardingCost * b - runningCost
#             print(a, b, cumulate,tryone,anotherone )
#             if profit > 0:
#                 rt=a+1
                
#             if tryone > anotherone:
#                 return a+1
#             else:
#                 return rt
        

