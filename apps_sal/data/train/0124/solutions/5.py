class Solution:
     def search(self, nums, target):
         """
         :type nums: List[int]
         :type target: int
         :rtype: bool
         """
         
         return self.bsearch(nums, target, 0, len(nums)-1)
         
     
     def bsearch(self, nums, target, left, right):
         
         if left > right:
             return False
         
         mid = (left+right)//2
         if nums[mid] == target:
             return True
         
         #print(nums[left], nums[mid], nums[right])
         if nums[left] < nums[mid]: # left sorted
             
             if nums[left] <= target <= nums[mid]:
                 return self.bsearch(nums, target, left, mid-1)
             else:
                 return self.bsearch(nums, target, mid+1, right)
         
         elif nums[mid] < nums[right]: # right sorted
             
             if nums[mid] <= target <= nums[right]:
                 return self.bsearch(nums, target, mid+1, right)
             else:
                 return self.bsearch(nums, target, left, mid-1)
         
         elif nums[mid] == nums[left]:
             return self.bsearch(nums, target, left+1, right)
         
         elif nums[mid] == nums[right]:
             return self.bsearch(nums, target, left, right-1)
         
         
             

