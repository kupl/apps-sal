class Solution:
     def minSubArrayLen(self, s, nums):
         """
         :type s: int
         :type nums: List[int]
         :rtype: int
         """
         
         
         prePtr = 0
         curPtr = 0
         
         curSum = 0
         
         res = float('inf')
         
         while curPtr < len(nums):
             
             curSum += nums[curPtr]
                 
             if curSum >= s:
                     
                 while curSum >= s:
                     curSum -= nums[prePtr]
                     prePtr += 1
                 prePtr -= 1
                 curSum += nums[prePtr]
                     
                 res = min(res, curPtr-prePtr+1)
                 
             curPtr += 1
         if res == float('inf'):
             return 0
         else:
             return res

