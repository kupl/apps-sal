class Solution:

    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows == 0:
            return []
        if numRows == 1:
            return [[1]]
        res = [[1], [1, 1]]

        def add(nums):
            res = nums[:1]
            for (i, j) in enumerate(nums):
                if i < len(nums) - 1:
                    res += [nums[i] + nums[i + 1]]
            res += nums[:1]
            return res
        while len(res) < numRows:
            res.append(add(res[-1]))
        return res
