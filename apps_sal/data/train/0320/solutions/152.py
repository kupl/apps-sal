from math import log


class Solution:

    def minOperations(self, nums: List[int]) -> int:
        cnt = int(log(max(nums)) / log(2))
        for n in nums:
            while n > 0:
                if n % 2 == 1:
                    n -= 1
                    cnt += 1
                else:
                    n = n // 2
        return cnt
