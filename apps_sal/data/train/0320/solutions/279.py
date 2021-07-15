class Solution:
    def minOperations(self, nums: List[int]) -> int:
        
        ops = 0
        N = len(nums)
        
        while True:
            n = 0
            alleven = True
            for i, num in enumerate(nums):
                if num == 0:
                    n += 1
                else:
                    if num % 2:
                        nums[i] -= 1
                        if num == 0: n += 1
                        alleven = False
                        ops += 1
                        
            if n == N:
                break 
            
            if alleven:
                for i in range(N):
                    if nums[i]:
                        nums[i] = nums[i] // 2
                ops += 1
        
        
        return ops

