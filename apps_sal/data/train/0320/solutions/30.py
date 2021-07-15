class Solution:
    def minOperations(self, nums: List[int]) -> int:
        # number of operation 1 (multiply by 2) is the length of bin(num)
        # number of operation 0 (increment by 1) is the number of 1 in bin(num)
        return sum(bin(num).count('1') for num in nums) + len(bin(max(nums))) - 3 # why 3, bin() function return a string leading by 0b10= => 4
