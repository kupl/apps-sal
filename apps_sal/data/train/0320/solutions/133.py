class Solution:
    def minOperations(self, nums: List[int]) -> int:
        steps = 0
        maxIdx, maxNum = None, -math.inf 
        
        for idx, num in enumerate(nums):
            if num > maxNum:
                maxNum = num
                maxIdx = idx
                
        nums[maxIdx], nums[-1] = nums[-1], nums[maxIdx]
        
        def divideBy2(nums):
            nums = [num // 2 for num in nums]
            return nums
        
        while nums[-1] > 0:
            for i in range(len(nums)):
                if nums[i] % 2 == 1:
                    nums[i] -= 1
                    steps += 1
                    
            if nums[-1] == 0:
                return steps
            
            nums = divideBy2(nums)
            steps += 1
            
        return steps
