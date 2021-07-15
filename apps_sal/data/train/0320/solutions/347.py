class Solution:
    def minOperations(self, nums: List[int]) -> int:
        self.count = 0
        all_even = False
        def reduce():
            nonlocal all_even
            zero = 0
            if all_even:
                for i, num in enumerate(nums):
                    nums[i] >>= 1
                    if nums[i] & 1:
                        all_even = False
                    zero += num == 0
                self.count += 1
            else:
                for i, num in enumerate(nums):
                    if num & 1:
                        self.count += 1
                        nums[i] -= 1
                all_even = True
            return zero
        
        while True:
            n = reduce()
            if n == len(nums):
                break
        return self.count - 1
            
                    
            
                    
                    

