class Solution:
    def minOperations(self, nums: List[int]) -> int:
        res = length = 0
        for num in nums:
            bits = bin(num)
            res += bits.count('1')
            length = max(length, len(bits)-2)
        return res + length -1
