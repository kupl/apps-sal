class Solution:
    def minOperations(self, nums: List[int]) -> int:

        count = 0
    
        while 1:
            
            for i, vi in enumerate(nums):
                
                if vi&1:
                    count += 1
                    nums[i] = vi - 1
                        
            
            chk = True
            
            for i, vi in enumerate(nums):
                if vi > 0:
                    chk = False
                nums[i] = vi // 2
                
            if chk:
                break
                
            count += 1
            
                
        return count

