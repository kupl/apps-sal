class Solution:
     def find132pattern(self, nums):
         """
         :type nums: List[int]
         :rtype: bool
         """
         min_nums = [0] * len(nums)
         for i, num in enumerate(nums):
             min_nums[i] = min(min_nums[i-1], num) if i else num
 
         stack = []
         for i, num in reversed(list(enumerate(nums))):
             while stack and stack[-1] <= min_nums[i]:
                 stack.pop()
             if stack and num > stack[-1]:
                 return True
             else:
                 stack.append(num)
 
         return False
