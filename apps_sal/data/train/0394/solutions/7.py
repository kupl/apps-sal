class Solution:
     def minMoves2(self, nums):
         """
         :type nums: List[int]
         :rtype: int
         """
         nums=sorted(nums)
         mid_x=nums[len(nums)//2]
 
         count=0
         for x in nums:
             count+=abs(x-mid_x)
         return count

