class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n_add, n_mul = 0, 0
        for num in nums:
            c_mul = 0
            while num > 1:
                n_add += num % 2
                num //= 2
                c_mul += 1
            if num == 1:
                n_add += 1
            n_mul = max(n_mul, c_mul)
        return n_add + n_mul
