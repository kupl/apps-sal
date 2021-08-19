class Solution:

    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        '\n         nums = sorted(nums)\n         size = len(nums)\n         res = list()\n         for i in range(size-2):\n             if i and nums[i] == nums[i-1]:\n                 continue\n             left, right = i+1, size-1\n             while left < right:\n                 sums = nums[i] + nums[left] + nums[right]\n                 if sums == target:\n                     return target\n                 else:\n                     res.append(sums)\n                     if sums < target:\n                         while left < right and nums[left] == nums[left+1]:\n                             left += 1\n                         left += 1\n                     else:\n                         while left < right and nums[right] == nums[right-1]:\n                             right -= 1\n                         right -= 1\n         return self.helper(res, target)\n     \n     def helper(self, nums, target):\n         if not nums:\n             return\n         goal = abs(nums[0] - target)\n         res = nums[0]\n         for num in nums[1:]:\n             if abs(num-target) < goal:\n                 goal = abs(num-target)\n                 res = num\n         return res\n \n         '
        nums = sorted(nums)
        size = len(nums)
        res = None
        diff = None
        for i in range(size - 2):
            if i and nums[i] == nums[i - 1]:
                continue
            (left, right) = (i + 1, size - 1)
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
                        (res, diff) = (tmp, abs(tmp - target))
                else:
                    partial = nums[i] + nums[left]
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    while left < right and partial + nums[right] > target:
                        right -= 1
                    tmp = partial + nums[right + 1]
                    if abs(tmp - target) < diff:
                        (res, diff) = (tmp, abs(tmp - target))
        return res
