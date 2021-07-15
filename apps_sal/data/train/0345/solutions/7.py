class Solution:
     def splitArray(self, nums, m):
         """
         :type nums: List[int]
         :type m: int
         :rtype: int
         """
         return self.use_binary_search(nums, m)
     
     def use_binary_search(self, nums, m):
         lo, hi = max(nums), sum(nums)
         
         while lo < hi:
             mid = lo + (hi - lo) // 2
             
             if self.valid(mid, nums, m):
                 hi = mid
             else:
                 lo = mid + 1
         return lo
     
     def valid(self, target, nums, m):
         total, count = 0, 1
         for num in nums:
             total += num
             if total > target:
                 total = num
                 count += 1
                 if count > m:
                     return False
         return True

