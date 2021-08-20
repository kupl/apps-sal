class Solution:

    def minOperations(self, nums: List[int]) -> int:
        twos = len(bin(max(nums))[2:]) - 1
        ones = collections.Counter(''.join((bin(i)[2:] for i in nums)))['1']
        return ones + twos
