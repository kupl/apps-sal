class Solution:
    def minOperations(self, nums: List[int]) -> int:
        # find number of set bits in all numbers
        # find offset of highest number
        if max(nums) == 0:
            return 0
        return sum(map(lambda x: bin(x).count('1'), nums)) + int(log2(max(nums)))
