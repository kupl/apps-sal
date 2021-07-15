class Solution:
    def minOperations(self, nums: List[int]) -> int:
        m = max(nums)
        n = nums.count(m)
        # as 'bin(len(5)) == 5'
        return sum(bin(a).count('1') for a in nums) + len(bin(max(nums))) - 3
    
    

