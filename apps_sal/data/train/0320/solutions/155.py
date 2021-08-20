class Solution:

    def minOperations(self, nums: List[int]) -> int:

        @lru_cache(None)
        def get(n):
            add = 0
            mul = 0
            while n:
                if n & 1:
                    add += 1
                    n -= 1
                else:
                    mul += 1
                    n = n >> 1
            return (add, mul)
        cadd = 0
        mmul = 0
        for n in nums:
            (add, mul) = get(n)
            cadd += add
            mmul = max(mul, mmul)
        return cadd + mmul
