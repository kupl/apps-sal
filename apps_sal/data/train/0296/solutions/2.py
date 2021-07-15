class Solution(object):
     def findMin(self, nums):
         """
         :type nums: List[int]
         :rtype: int
         """
         if len(nums) == 1:
             return nums.pop()
 
         start, finish = 1, len(nums) - 1
 
         while start < finish:
             half = (start + finish) // 2
             if nums[half] > nums[0]:
                 start = half + 1
             elif nums[half] == nums[0]:
                 return min(Solution.findMin(self, nums[:half]), Solution.findMin(self, nums[half:]))
             else:
                 finish = half
 
         return min(nums[start], nums[0])

