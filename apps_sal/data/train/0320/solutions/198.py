class Solution:
    def minOperations(self, nums: List[int]) -> int:
        ops = 0
        done = False
        while not done:
            # Make nums all even numbers
            for i in range(len(nums)):
                if nums[i] % 2:
                    nums[i] -= 1
                    ops += 1
            # Divide nums by 2
            done = True
            for i in range(len(nums)):
                if nums[i] != 0:
                    done = False
                    nums[i] /= 2
            if not done:
                ops += 1
        return ops
            
                    
            

