class Solution:
    def possibleWithinDays(self, weights, D, capacity):
        x = 0
        i = 1
        total = 0
        while(i <= D):
            current_sum = 0
            #print(i)
            
            while(x < len(weights) and current_sum + weights[x] <= capacity):
                current_sum += weights[x]
                total += weights[x]
                x += 1
            #print(\"x: \",x)
            #print(\"cur_sum: \",current_sum)
            #print(\"total: \",total)
            i += 1
        
        if total >= sum(weights):
                return True
        #print(\"i\",i,\"x\",x)
        return False
            
    
    def shipWithinDays(self, weights: List[int], D: int) -> int:
        total_sum = sum(weights)
        left = 0
        right = total_sum
        
        while(left < right):
            middle = (left+right)//2
            aux = self.possibleWithinDays(weights,D,middle)
            if aux:
                right = middle
            else:
                left = middle+1
        
        return left
        
    #1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 ...50000 
    #1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 ... 55
    #that capacity makes True if we can do it in less or equal than D
   
    #1+55 = 56/2 = 28

