class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], X: int) -> int:
        N = len(customers)
        satisfy = 0
        unsatisfied = []
        max_value = 0
        #Base cases
        if not customers:
            return []
        elif not grumpy or N==1:
            return sum(customers)
        
        
        for i in range(N):
            if grumpy[i] == 0:
                satisfy += customers[i]
                unsatisfied.append(0)
                
            else:
                unsatisfied.append(customers[i])
                
            
        for j in range(N-X+1):
            sum1 = sum(unsatisfied[j:j+X])
            
            max_value = max(max_value,sum1)
        return (satisfy + max_value)
        
                
            

