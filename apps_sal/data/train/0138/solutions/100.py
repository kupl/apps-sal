class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        i = 0
        j = 0
        minus = 0
        res = 0
        
        while j < len(nums):
            if nums[j] < 0:
                minus+=1
                j+=1
            elif nums[j] > 0:
                j+=1
            else:
                minus = 0
                i = j+1
                j = i
            if minus%2==0:
                res = max(res, j-i)
                
        
        if minus%2==0:
            res = max(res, j-i)
        
        minus = 0
        i = len(nums)-1
        j = len(nums)-1
        
        while j >= 0:
            if nums[j] < 0:
                minus+=1
                j-=1
            elif nums[j] > 0:
                j-=1
            else:
                minus = 0
                i = j-1
                j = i
            if minus%2==0:
                res = max(res, i-j)
                
        
        if minus%2==0:
            res = max(res, i-j)
            
        return res
            

