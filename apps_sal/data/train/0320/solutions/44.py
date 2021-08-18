class Solution:
    def minOperations(self, nums: List[int]) -> int:
        two, one = 0, 0
        for n in nums:
            mul = 0
            while n:
                if n % 2:
                    one += 1
                    n -= 1
                else:
                    mul += 1
                    n //= 2
            two = max(two, mul)
        return one + two
