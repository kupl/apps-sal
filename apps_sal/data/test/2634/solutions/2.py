class Solution:
     def subsets(self, nums):
         """
         :type nums: List[int]
         :rtype: List[List[int]]
         """
         result = [[]]
         for num in nums:
             result += self.get_subset(result, num)
         return result
         
     def get_subset(self, subsets, item):
         
         new_subset_with_item = []
         for subset in subsets:
             new_subset_with_item.append(subset + [item])
         
         return new_subset_with_item
         

