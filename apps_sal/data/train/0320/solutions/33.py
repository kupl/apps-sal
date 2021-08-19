class Solution:

    def minOperations(self, nums: List[int]) -> int:
        (maxLmove, bitCount) = (0, 0)
        for num in nums:
            if num == 0:
                continue
            Lmove = 0
            while num != 0:
                if num & 1:
                    bitCount += 1
                num = num >> 1
                if num != 0:
                    Lmove += 1
            maxLmove = max(maxLmove, Lmove)
        return maxLmove + bitCount
