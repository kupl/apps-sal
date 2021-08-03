class Solution:
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        '''
         sums = sum(nums)
         if sums & 1:
             return False
         target = sums//2
         if max(nums) > target:
             return False
         elif max(nums) == target:
             return True
         target -= max(nums)
         nums = [num for num in nums if num <= target]
         if not nums:
             return False
         if target in nums:
             return True
         pool = set([0])
         for num in nums:
             for p in pool.copy():
                 pool.add(num+p)
         return target in pool
         '''
        '''
         s = sum(nums)
         if s & 1:
             return False
         target = s//2
         pool = set([0])
         for num in nums:
             for p in pool.copy():
                 pool.add(num+p)
         return target in pool
         '''
        s = sum(nums)
        if s & 1:
            return False
        target = s // 2
        cnt = collections.Counter(nums)
        return self.helper(target, cnt)

    def helper(self, target, cnt):
        if target == 0:
            return True
        if target < 0:
            return False
        for item in sorted(list(cnt.keys()), reverse=True):
            if cnt[item] == 0:
                continue
            cnt[item] -= 1
            if self.helper(target - item, cnt):
                return True
            cnt[item] += 1
        return False
