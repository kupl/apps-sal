class Solution:
    def minOperationsMaxProfit(self, cus: List[int], boardingCost: int, runningCost: int) -> int:
        
        for i in range(1, len(cus)):
            cus[i]+=cus[i-1]
        
        cus = cus + [cus[-1]]*(len(cus)*50)
        i = 0
        profit = [0]
        used = 0
        flag = 0
        while True and i<len(cus):
            
            
            cust = min(4, cus[i]-used)
            if cust<=0 and flag == 1:
                break
            if cust == 0:
                flag = 1
                
            used += cust
            cost = cust*boardingCost
            p = cost-runningCost            
            profit.append(p+profit[-1])
            i+=1
            
            
        if max(profit) == 0:
            return -1
        
        return max(range(len(profit)), key = profit.__getitem__)
