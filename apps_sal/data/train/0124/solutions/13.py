class Solution:
     def search(self, nums, target):
         """
         :type nums: List[int]
         :type target: int
         :rtype: bool
         """
         if (not nums):
             return False
         i = 0
         while (i + 1 < len(nums) and nums[i] == nums[i + 1]):
             i += 1
         if (i + 1 == len(nums)):
             # nums中所有元素相等
             return nums[0] == target
         
         # 找到最大元素的位置
         l, r = i, len(nums) - 1
         while (l + 1 < r):
             mid = l + (r - l) // 2
             if (nums[i] < nums[mid]):
                 l = mid
             else:
                 r = mid - 1
         highest_pos = l if (nums[l] > nums[r]) else r
         
         if (target >= nums[0]):
             return self._binarySearch(nums, 0, highest_pos, target)
         else:
             return self._binarySearch(nums, highest_pos + 1, len(nums) - 1, target)
         
         
     def _binarySearch(self, nums, l, r, target):
         while (l <= r):
             mid = l + (r - l) // 2
             if (nums[mid] < target):
                 l = mid + 1
             elif (nums[mid] > target):
                 r = mid - 1
             else:
                 return True
         return False

