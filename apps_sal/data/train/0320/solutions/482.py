class Solution:
    def minOperations(self, nums: List[int]) -> int:
        return sum(bin(a).count('1') for a in nums) + len(bin(max(nums))) - 3
