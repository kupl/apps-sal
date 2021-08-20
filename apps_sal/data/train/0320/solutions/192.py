class Solution:

    def minOperations(self, nums: List[int]) -> int:
        """Reverse thinking, from result number back to zeros"""
        'Time:O(n*n/2)->O(n^2), Space:O(1)'
        'Time:O(n), Space:O(1)'
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
