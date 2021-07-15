class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], X: int) -> int:
        if len(customers) <= X:
            return sum(customers)
        
        
        satisfied_customers = 0
        current_unsatisfied_customers = 0
        max_unsatisfied_customers = 0
        
        for i in range(len(customers)):
            if i >= X and grumpy[i-X] == 1:
                current_unsatisfied_customers -= customers[i-X]
                
            if grumpy[i] == 0:
                satisfied_customers += customers[i]
            else:
                current_unsatisfied_customers += customers[i]
                
            max_unsatisfied_customers = max(max_unsatisfied_customers, current_unsatisfied_customers)
            
        return satisfied_customers + max_unsatisfied_customers
                
        
            

