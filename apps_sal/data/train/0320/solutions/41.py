class Solution:

    def minOperations(self, nums: List[int]) -> int:
        if max(nums) == 0:
            return 0
        return sum(map(lambda x: bin(x).count('1'), nums)) + int(log2(max(nums)))
