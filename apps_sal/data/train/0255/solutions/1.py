class Solution:

    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = 0
        n = len(nums)
        (i, j) = (0, 0)
        while j < n - 1:
            print((i, j))
            (ii, jj) = (i, j)
            for k in range(ii, jj + 1):
                j = max(j, min(n - 1, k + nums[k]))
            i = jj + 1
            res += 1
        return res
