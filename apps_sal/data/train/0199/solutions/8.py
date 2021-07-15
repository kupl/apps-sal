class Solution:
     def longestConsecutive(self, nums):
         """
         :type nums: List[int]
         :rtype: int
         """
         s = set(nums)
         
         longest = 0
         for i in s: 
             if(i-1 in s):
                 continue
             sequence = 1
             num = i
             while(num+1 in s):
                 sequence += 1
                 num += 1
             longest = max(longest, sequence)
             
         return longest
