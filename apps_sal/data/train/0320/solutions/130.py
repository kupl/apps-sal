bin = '{:0b}'.format


class Solution:
    def minOperations(self, nums: List[int]) -> int:
        maxBitLen = 0
        bitCount = 0
        for num in nums:
            b = bin(num)
            maxBitLen = max(maxBitLen, len(b))
            bitCount += b.count('1')
        return maxBitLen + bitCount - 1
