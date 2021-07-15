class Solution:
     def maximumGap(self, nums):
         """
         :type nums: List[int]
         :rtype: int
         """
         n = len(nums)
         if n == 0:
             return 0
         buckets = [{"min": None, "max": None} for _ in range(n)]
         n_min = min(nums)
         n_max = max(nums)
         if n_max == n_min:
             return 0
         for num in nums:
             i = (num - n_min) * (n - 1) // (n_max - n_min)
             if buckets[i]["min"] is None:
                 buckets[i]["min"] = num
                 buckets[i]["max"] = num
             else:
                 buckets[i]["min"] = min(num, buckets[i]["min"])
                 buckets[i]["max"] = max(num, buckets[i]["max"])
         max_diff = 0
         max_prev = buckets[0]["max"]
         for i in range(1, n):
             if buckets[i]["min"] is not None:
                 max_diff = max(max_diff, buckets[i]["min"]-max_prev)
                 max_prev = buckets[i]["max"]
         #print(buckets)
         return max_diff
