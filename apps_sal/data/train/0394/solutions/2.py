class Solution:
     def minMoves2(self, nums):
         """
         :type nums: List[int]
         :rtype: int
         """
         mid = len(nums) // 2
         tar = sorted(nums)[mid]
         return sum([abs(x - tar) for x in nums])

