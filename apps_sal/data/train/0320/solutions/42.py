class Solution:
    def minOperations(self, nums: List[int]) -> int:
        op0 = 0
        op1 = 0
        for n in nums:
            l = 0
            while n > 0:
                l += 1
                if n % 2 == 1: op0 += 1
                n //= 2
            op1 = max(op1, l-1)
        return op0 + op1
