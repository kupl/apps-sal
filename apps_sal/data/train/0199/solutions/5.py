class Solution:
     def longestConsecutive(self, nums):
         """
         :type nums: List[int]
         :rtype: int
         """
         flag_map = {}
         for x in nums:
             flag_map[x] = False
         
         result = 0
         for x in nums:
             count = 1
             tmp = x + 1
             flag_map[x] = True
             while True:
                 if tmp in flag_map and not flag_map[tmp]:
                     count = count + 1
                     flag_map[tmp] = True
                     tmp = tmp + 1
                 else:
                     break
                     
             tmp = x - 1
             while True:
                 if tmp in flag_map and not flag_map[tmp]:
                     count = count + 1
                     flag_map[tmp] = True
                     tmp = tmp - 1
                 else:
                     break
                     
             result = max(result, count)
             
         return result
