class Solution:
    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        index = 1 
        profit = []
        esperan = 0 
        personas = 0
        suben = 0
        
        for i in customers:
            suben = esperan + i
            if suben>=4:
                esperan = abs(esperan + i - 4)
                personas +=4
                
                
            else:
                if esperan - i<0:
                    esperan = 0
                else:
                    esperan = abs(esperan - i)
                personas +=i
            profit.append(personas*boardingCost-index*runningCost)
            
            index+=1
        
        for i in range(int(esperan/4)):
            
            suben = esperan 
            if suben>=4:
                esperan = abs(esperan- 4)
                personas +=4
                
                
            else:
                if esperan - i<0:
                    esperan = 0
                else:
                    esperan = esperan - i
                personas +=i
            profit.append(personas*boardingCost-index*runningCost)
            
            index+=1
            
        
        if esperan>0:
            profit.append((personas+esperan)*boardingCost-index*runningCost)
        
        if max(profit)<0:
            return -1
        
      
        else:
            return profit.index(max(profit))+1

