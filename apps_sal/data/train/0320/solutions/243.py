import math


class Solution:
    def minOperations(self, nums: List[int]) -> int:
        p = []
        ans = 0
        for i in nums:
            r = 0
            while(i > 0):
                if (i % 2 == 0):
                    r += 1
                    i /= 2
                else:
                    ans += 1
                    i -= 1
            p.append(r)

        ans += max(p)
        return ans
