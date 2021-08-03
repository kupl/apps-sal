class Solution:
    def minOperations(self, nums: List[int]) -> int:
        twos = 0
        ones = 0
        for n in nums:
            mul = 0
            while n:
                if n % 2:
                    n -= 1
                    ones += 1
                else:
                    n //= 2
                    mul += 1
            twos = max(twos, mul)
        return ones + twos


# class Solution:
#     def minOperations(self, nums: List[int]) -> int:
#         twos = 0
#         ones = 0
#         for n in nums:
#             mul = 0
#             while n:
#                 if n%2: # odd number, just delete 1 so that it's now a multiple of 2
#                     n -= 1
#                     ones += 1
#                 else: # multiple of 2, so just divide by 2
#                     n //= 2
#                     mul += 1
#             twos = max(twos, mul)
#         return ones + twos
