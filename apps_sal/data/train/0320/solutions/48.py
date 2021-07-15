class Solution:
    def minOperations(self, nums: List[int]) -> int:
        
        total = 0
        currentMax = 0
        for n in nums:
            if n == 0:
                continue 
            total += 1
            count = 0
            while n > 1:
                if n % 2 == 1:
                    n -= 1
                    total += 1
                n = n //2
                count += 1
            
            currentMax = max(count, currentMax)
        return total + currentMax
            
                
        
            

