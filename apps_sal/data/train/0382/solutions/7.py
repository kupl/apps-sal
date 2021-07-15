class Solution:
     def findPeakElement(self, nums):
         """
         :type nums: List[int]
         :rtype: int
         """
         if len(nums) == 1:
             return 0
         left, right = 0, len(nums) - 1
         length = len(nums)
         while left + 1 < right:
             mid = (left + right) // 2
             if mid == 0:
                 if nums[mid] > nums[mid + 1]:
                     return 0
                 else:
                     left = mid + 1
             elif mid == length - 1:
                 if nums[-1] > nums[-2]:
                     return mid
                 else:
                     right = mid - 1
             elif nums[mid] > nums[mid - 1] and nums[mid] > nums[mid + 1]:
                 return mid
             elif nums[mid] < nums[mid - 1] and nums[mid] < nums[mid + 1]:
                 right = mid - 1
             elif nums[mid] > nums[mid + 1]:
                 right = mid - 1
             else:
                 left = mid + 1
         for idx in range(left, right + 1):
             if idx == 0 and nums[idx] > nums[idx + 1]:
                 return 0
             if idx == length - 1 and nums[-1] > nums[-2]:
                 return idx
             if nums[idx] > nums[idx - 1] and nums[idx] > nums[idx + 1]:
                 return idx
