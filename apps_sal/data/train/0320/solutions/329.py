class Solution:
    def minOperations(self, nums: List[int]) -> int:
        ones = 0
        twos = 0

        for n in nums:
            muls = 0
            while n > 0:
                if n % 2 != 0:
                    ones += 1
                    n -= 1
                else:
                    muls += 1
                    n /= 2

            twos = max(muls, twos)

        return ones + twos
