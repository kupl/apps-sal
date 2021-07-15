class Solution:
     def search(self, nums, target):
         """
         :type nums: List[int]
         :type target: int
         :rtype: int
         """
         if not nums:
             return -1
         
         # [4,5,6,7,0,1,2]
         # 0
         start, end = 0, len(nums) - 1
         while start + 1 < end:
             mid = start + (end - start) // 2
             if target < nums[end]:
                 if nums[mid] < target or nums[mid] > nums[end]:
                     start = mid
                 elif nums[mid] > target and nums[mid] < nums[end]:
                     end = mid
                 else:
                     return mid
             elif target > nums[end]:
                 if nums[mid] > target or nums[mid] < nums[end]:
                     end = mid
                 elif nums[mid] < target and nums[mid] > nums[end]:
                     start = mid
                 else:
                     return mid
             else:
                 return len(nums) - 1
         
         if nums[start] == target:
             return start
         if nums[end] == target:
             return end
         
         return -1
