class Solution:

    def minOperations(self, nums: List[int]) -> int:
        max_ = max(nums)
        multiplication = len(bin(max_)[2:]) - 1
        additions = 0
        for n in nums:
            additions += bin(n)[2:].count('1')
        return additions + multiplication
