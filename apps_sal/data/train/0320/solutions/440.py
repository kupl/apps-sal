from math import floor, log


class Solution:

    def minOperations(self, nums: List[int]) -> int:
        ans = 0
        for x in nums:
            for i in bin(x)[2:]:
                if i != '0':
                    ans += 1
        m = max(nums)
        ans += floor(log(m, 2))
        return ans
