class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], X: int) -> int:
        n = len(customers)
        if n == 0:
            return 0
        
        running_sum = 0
        
        for i in range(n):
            if i < X:
                running_sum += customers[i]
            else:
                running_sum += customers[i] * (1-grumpy[i])
                
        left, right = 0, X
        ans = running_sum
        
        while right < n:
            if grumpy[right] == 1:
                running_sum += customers[right]
            right += 1
            
            if grumpy[left] == 1:
                running_sum -= customers[left]
            
            left += 1
        
            ans = max(ans, running_sum)
            
        return ans
