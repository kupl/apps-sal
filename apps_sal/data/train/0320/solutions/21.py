import math


class Solution:
    def minOperations(self, nums: List[int]) -> int:
        count = max([int(math.log(x) / math.log(2)) for x in nums if x > 0])
        for n in nums:
            while (n):
                if n % 2:
                    count += 1
                    n -= 1
                else:
                    n //= 2
        return count
