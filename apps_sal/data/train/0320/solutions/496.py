from math import log2 as l


class Solution:

    def minOperations(self, nums: List[int]) -> int:
        cnt = 0
        mx = max(nums)
        if mx & 1 and mx != 1:
            mx -= 1
        for x in nums:
            while x:
                if x & 1:
                    cnt += 1
                x //= 2
        return int(l(mx)) + cnt
