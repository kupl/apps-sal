class Solution:
    def clumsy(self, N: int) -> int:
        result = N
        
        product_part = 0
        sum_part = 0
        
        def g(x):
            return N - x + 1
        
        for i in range(0, ceil(N / 4)):
            nums = list(range(4 * i + 1, min(4 * i + 5, N + 1)))
            
            p = g(nums[0])
            s = 0
            if len(nums) > 1:
                p *= g(nums[1])
            if len(nums) > 2:
                p //= g(nums[2])
            if len(nums) > 3:
                s = g(nums[3])
                
            if i > 0:
                p *= -1
            
            product_part += p
            sum_part += s
        
        return product_part + sum_part
