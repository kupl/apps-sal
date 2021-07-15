class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n_add = 0
        n_mul = 0
        for n in nums:
            mul = 0
            while n > 0:
                if n % 2:
                    n -= 1
                    n_add += 1
                else:
                    mul += 1
                    n //= 2
            n_mul = max(n_mul, mul)
        return n_add + n_mul
