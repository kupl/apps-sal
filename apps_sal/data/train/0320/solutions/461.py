class Solution:
    def minOperations(self, nums: List[int]) -> int:
        add = 0
        mul = 0
        for n in nums:
            m = 0
            while n > 0:                
                if (n & 1) == 1:
                    add += 1
                    n -= 1
                else:
                    m += 1
                    mul = max(m, mul)
                    n //= 2
        return add + mul
                    

