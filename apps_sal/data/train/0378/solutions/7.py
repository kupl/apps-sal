class Solution:

    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        '\n         sums = sum(nums)\n         if sums & 1:\n             return False\n         target = sums//2\n         if max(nums) > target:\n             return False\n         elif max(nums) == target:\n             return True\n         target -= max(nums)\n         nums = [num for num in nums if num <= target]\n         if not nums:\n             return False\n         if target in nums:\n             return True\n         pool = set([0])\n         for num in nums:\n             for p in pool.copy():\n                 pool.add(num+p)\n         return target in pool\n         '
        '\n         s = sum(nums)\n         if s & 1:\n             return False\n         target = s//2\n         pool = set([0])\n         for num in nums:\n             for p in pool.copy():\n                 pool.add(num+p)\n         return target in pool\n         '
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
