class Solution:
    def minOperations(self, nums: List[int]) -> int:
        
        result = 0;  
        n = len(nums)
        while True : 
            zeros = 0   
            i = 0 
            while (i < n) :   
                if nums[i] % 2 :  
                    break   
                    
                elif nums[i] == 0 :  
                    zeros += 1 
                i += 1 
                
            if (zeros == n):  
                return result   
  
            if (i == n):  
 
                for j in range(n): 
                    nums[j] = nums[j] // 2;  
                result += 1 
  
            for j in range(i, n):  
                if nums[j] % 2 :  
                    nums[j] -= 1  
                    result += 1  

