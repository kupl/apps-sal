class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        prev = 0
        prev_zero = 0
        result = float('-inf')
        boolean = False
        count = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                boolean = True
                count+= 1
                if count == 2:
                    count-= 1
                    prev = prev_zero + 1
                prev_zero = i
                
            result = max(result,i - prev)
        
        return result if boolean == True else len(nums)-1
            
            

