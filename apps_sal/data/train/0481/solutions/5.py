class Solution:
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        '''
         nums = sorted(nums)
         size = len(nums)
         res = list()
         for i in range(size-2):
             if i and nums[i] == nums[i-1]:
                 continue
             left, right = i+1, size-1
             while left < right:
                 sums = nums[i] + nums[left] + nums[right]
                 if sums == target:
                     return target
                 else:
                     res.append(sums)
                     if sums < target:
                         while left < right and nums[left] == nums[left+1]:
                             left += 1
                         left += 1
                     else:
                         while left < right and nums[right] == nums[right-1]:
                             right -= 1
                         right -= 1
         return self.helper(res, target)
     
     def helper(self, nums, target):
         if not nums:
             return
         goal = abs(nums[0] - target)
         res = nums[0]
         for num in nums[1:]:
             if abs(num-target) < goal:
                 goal = abs(num-target)
                 res = num
         return res
 
         '''
        nums = sorted(nums)
        size = len(nums)
        res = None
        diff = None
        for i in range(size - 2):
            if i and nums[i] == nums[i - 1]:
                continue
            left, right = i + 1, size - 1
            if not diff:
                res = nums[i] + nums[left] + nums[right]
                diff = abs(res - target)
            while left < right:
                sums = nums[i] + nums[left] + nums[right]
                if sums == target:
                    return target
                elif sums < target:
                    partial = nums[i] + nums[right]
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and partial + nums[left] < target:
                        left += 1
                    tmp = partial + nums[left - 1]
                    if abs(tmp - target) < diff:
                        res, diff = tmp, abs(tmp - target)
                else:
                    partial = nums[i] + nums[left]
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    while left < right and partial + nums[right] > target:
                        right -= 1
                    tmp = partial + nums[right + 1]
                    if abs(tmp - target) < diff:
                        res, diff = tmp, abs(tmp - target)
        return res
