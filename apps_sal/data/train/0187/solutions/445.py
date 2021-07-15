import math
class Solution:
    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        x = sum(customers)
        a = []
        r =0
        p = 0
        for i in range(len(customers)):
            if r>=i:
                p+=customers[i]
                a.append(min(4,p))
                if p>=4:
                    p-= 4
                else:
                    p-=customers[i]
                # print(p)
            else:
                a.append(0)
            r+=1
        # print(p)
        while p>0:
            a.append(min(4,p))
            p-=4
        rotations = len(a)
        
        
            
        loss =[ ]    
        for i in range(1,rotations+1):
            loss.append(runningCost*i)
        
        for i in range(1,len(a)):
            a[i] = a[i-1]+a[i]
        
        res = -1
        index = -2
        print((len(loss),rotations,len(a)))
        for i in range(rotations):
            if res< a[i]*boardingCost-loss[i]:
                res = a[i]*boardingCost-loss[i]
                index = i
                
        return index+1
            
            
        
    
        
        
            

