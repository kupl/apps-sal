masks = [1431655765, 858993459, 252645135, 16711935, 65535]


class Solution:

    def minOperations(self, nums: List[int]) -> int:
        totOddRem = 0
        max2Power = 0
        for x in nums:
            if x == 1:
                totOddRem += 1
            else:
                leftMost = 0
                step = 16
                xCopy = x
                for m in reversed(masks):
                    mr = ~m
                    if mr & xCopy != 0:
                        leftMost += step
                        xCopy &= mr
                    step >>= 1
                if leftMost > max2Power:
                    max2Power = leftMost
                xCopy = x
                for (p, m) in enumerate(masks):
                    xCopy = (xCopy & m) + ((xCopy & ~m) >> (1 << p))
                totOddRem += xCopy
        return totOddRem + max2Power
