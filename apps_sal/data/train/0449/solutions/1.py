class Solution:
     def findMin(self, nums):
         """
         :type nums: List[int]
         :rtype: int
         """
         if len(nums) == 0:
             return None
         
         # case 1: minimum element is at index 0
         # case 2: minimum element is at pivot index
         #     4 5 6 7   0 1 2
         #             |<-  every element after here is < element at index 0
         #     tail    |  head
         
         # => check for case 1:
         if nums[-1] > nums[0]:
             return nums[0]
         
         # case 2. binary search for the start of the pivoted sequence
         boundary = nums[0]
         return self.binary_search_min(nums, boundary)
         
     def binary_search_min(self, nums, maximum):
         """
         Binary search for the minimum element, assuming that every element >= maximum indicates leaving the array to the left
         """        
         left_boundary = 0
         right_boundary = len(nums) - 1
         
         while True:
             current_index = left_boundary + (right_boundary - left_boundary) // 2
             value = nums[current_index]
             
             if left_boundary == right_boundary:
                 return value
             
             if value >= maximum:
                 # we hit the tail end, search further to the right
                 left_boundary = current_index + 1
             else:
                 # still in the head, search further to the left
                 right_boundary = current_index 
             
             
         
         

