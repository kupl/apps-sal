class Solution:
     def canPartitionKSubsets(self, nums, k):
         """
         :type nums: List[int]
         :type k: int
         :rtype: bool
         """
         
         if not nums:
             return True
         
         if sum(nums) % k != 0:
             return False
         
         target = sum(nums) / k
         
         nums.sort()
         
         if nums[-1] > target:
             return False
         
         while nums and nums[-1] == target:
             nums.pop()
             k -= 1
         
         def partition(nums, subsets, target):
             if not nums:
                 return True
             selected = nums.pop()
             for i in range(len(subsets)):
                 if subsets[i] + selected <= target:
                     subsets[i] += selected
                     if partition(nums, subsets, target):
                         return True
                     subsets[i] -= selected
                 if subsets[i] == 0:
                     # this line is important, otherwise TLE.
                     # if subsets[i] is 0 then later subsets are all zeros. No need to try them all.
                     break
             nums.append(selected)
             return False
         
         return partition(nums, subsets=[0]*k, target=target)
