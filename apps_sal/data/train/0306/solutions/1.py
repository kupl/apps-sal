class Solution:

    def combinationSum4(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        record = {0: 1}

        def helper(target):
            if target in record:
                return record[target]
            res = 0
            for x in nums:
                if target >= x:
                    res += helper(target - x)
            record[target] = res
            return res
        return helper(target)
