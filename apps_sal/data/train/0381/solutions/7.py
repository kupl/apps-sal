class Solution:
     # this one is really easy to confuse you to apply greedy method. The greed method will start from the whole string and delete the smaller one of the start and the end element. This is wrong since there could be a case that at one end there are two mid-range number that sum over s while at the other end there are a big number and a smalle one which do not sum over s. The greedy method will delete the first mid-range number hence provide the wrong answer.
     
     # instead, one could apply the following algorithm: start from the beginning, add nums[i] to sum, if sum is greater than s, we keep substracting from the beginning of the current subarray until the sum is no greater thans, then we keep moving i to the next one unitl the sum is greater than s again. 
     def minSubArrayLen(self, s, nums): 
         """
         :type s: int
         :type nums: List[int]
         :rtype: int
         """
         if not nums or sum(nums)<s:
             return 0
         ans=len(nums)
         left=0
         temps=0
         for i in range(len(nums)):
             temps+=nums[i]
             while temps>=s:
                 ans=min(ans,i+1-left)
                 temps-=nums[left]
                 left+=1
         return ans

