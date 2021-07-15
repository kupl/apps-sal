class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], X: int) -> int:
        curr_running_delta = 0
        max_delta = (-2**31, None) # max sum, end idx
        
        for i in range(len(customers)):
            curr_running_delta += customers[i]*grumpy[i]
            
            if i >= X - 1:
                if curr_running_delta > max_delta[0]:
                    max_delta = (curr_running_delta, i)
                
                if grumpy[i - (X-1)] == 1:
                    curr_running_delta -= customers[i - (X-1)]
        
        max_satisfied = 0
        for i in range(len(customers)):
            if max_delta[1] - (X-1) <= i <= max_delta[1] or grumpy[i] == 0:
                max_satisfied += customers[i]
                
        return max_satisfied
    
    # time O(n)
    # space O(1)

