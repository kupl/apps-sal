class Solution:
    def getMaxLen(self, nums):
        
        if len(nums) == 0:
            return True
        
        result = 0
        count = 0
        zero_marker = -1
        negative_marker = -1
       
        for i in range(len(nums)):
            if nums[i] == 0:
                zero_marker = i
                count = 0
                negative_marker = -1
                

            else:
                if nums[i] < 0:
                    count += 1
                    if negative_marker == -1:
                        negative_marker = i
            
                if count % 2 == 0:
                    result = max(result, i - zero_marker)
                else:
                    result = max(result, i - negative_marker)
        return result      
