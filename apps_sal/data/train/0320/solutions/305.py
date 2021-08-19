masks = [1431655765, 858993459, 252645135, 16711935, 65535]


class Solution:

    def minOperations(self, nums: List[int]) -> int:
        totOddRem = 0
        maxX = nums[0]
        for x in nums:
            if x == 1:
                totOddRem += 1
            else:
                xCopy = x
                for (p, m) in enumerate(masks):
                    xCopy = (xCopy & m) + ((xCopy & ~m) >> (1 << p))
                totOddRem += xCopy
            if x > maxX:
                maxX = x
        leftMost = 0
        step = 16
        for m in reversed(masks):
            mr = ~m
            if mr & maxX != 0:
                leftMost += step
                maxX &= mr
            step >>= 1
        return totOddRem + leftMost
