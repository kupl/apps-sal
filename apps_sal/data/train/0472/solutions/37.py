class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        
        nums = arr
        update = True
        while update:
            update = False
            for i in range(len(nums)):
                j = nums[i]
                if nums[i] == 0:
                    continue
                
                if i-j>=0 and nums[i-j]==0:
                    nums[i] = 0
                    update = True
                    
            for i in reversed(list(range(len(nums)))):
                j = nums[i]
                if nums[i] == 0:
                    continue
                
                if i+j<len(nums) and nums[i+j]==0:
                    nums[i] = 0
                    update = True
        
        return nums[start] == 0
                    

