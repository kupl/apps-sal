class Solution:

    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        _sum = sum(nums)
        (div, mod) = divmod(_sum, 2)
        if mod != 0:
            return False
        target = [div] * 2
        self._len = len(nums)
        nums.sort(reverse=True)

        def dfs(index, target):
            if index == self._len:
                return True
            num = nums[index]
            for i in range(2):
                if target[i] >= num:
                    target[i] -= num
                    if dfs(index + 1, target):
                        return True
                    target[i] += num
            return False
        return dfs(0, target)
