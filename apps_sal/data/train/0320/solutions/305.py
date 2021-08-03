masks = [0b01010101010101010101010101010101,
         0b00110011001100110011001100110011,
         0b00001111000011110000111100001111,
         0b00000000111111110000000011111111,
         0b00000000000000001111111111111111]


class Solution:
    def minOperations(self, nums: List[int]) -> int:
        totOddRem = 0
        maxX = nums[0]
        for x in nums:
            if x == 1:
                totOddRem += 1
            else:
                xCopy = x
                for p, m in enumerate(masks):
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
