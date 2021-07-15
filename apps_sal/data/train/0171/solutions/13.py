class Solution:
     def maxProduct(self, nums):
         """
         :type nums: List[int]
         :rtype: int
         """
         largestproduct = []
         smallestproduct = []
         n =len(nums)
         largestproduct.append(nums[0])
         smallestproduct.append(nums[0])
         for i in range(n-1):
             lp = max(max(largestproduct[i]*nums[i+1],smallestproduct[i]*nums[i+1]),nums[i+1])
             sp = min(min(largestproduct[i]*nums[i+1],smallestproduct[i]*nums[i+1]),nums[i+1])
             largestproduct.append(lp)
             smallestproduct.append(sp)
         sol = largestproduct[0]
         for i in range(n):
             sol = max(sol,largestproduct[i])
         return sol

