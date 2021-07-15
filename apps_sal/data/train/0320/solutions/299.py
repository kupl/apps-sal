class Solution:
    def minOperations(self, nums: List[int]) -> int:
        num_operations = 0
        
        odd = True
        even = False
        
        while odd or even:
            if odd:
                for i in range(len(nums)):
                    if nums[i] != 0:
                        if nums[i] % 2:
                            nums[i] -= 1
                            num_operations += 1
                        if nums[i]:
                            even = True
                odd = False
                
            if even:
                num_operations += 1
                for i in range(len(nums)):
                    nums[i] /= 2
                    if nums[i] % 2:
                        even = False
                        odd = True
                        
        
        return num_operations
