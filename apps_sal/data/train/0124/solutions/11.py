class Solution:
     def search(self, nums, target):
         """
         :type nums: List[int]
         :type target: int
         :rtype: bool
         """
         if len(nums) == 0:
             return False
         def binary_search(leftIndex, rightIndex):
             midIndex = int((rightIndex+leftIndex)/2)
             if nums[midIndex] == target:
                 return True
             if leftIndex > rightIndex:
                 return False
             return binary_search(leftIndex, midIndex-1) or binary_search(midIndex+1, rightIndex)
         return binary_search(0, len(nums)-1)

