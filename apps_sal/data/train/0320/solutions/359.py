from math import log


class Solution:

    def minOperations(self, nums: List[int]) -> int:
        max2 = 0
        count = 0
        for n in nums:
            n_mult2 = 0
            while n != 0:
                if n % 2 == 0:
                    n = n / 2
                    n_mult2 += 1
                else:
                    n = n - 1
                    count += 1
            max2 = max(max2, n_mult2)
        return count + max2
