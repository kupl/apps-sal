class Solution:

    def getMaxLen(self, nums: List[int]) -> int:

        def helper(nums):
            if len(nums) == 0:
                return 0
            pre_prod = 1
            N = len(nums)
            first_neg = -1
            res = 0
            for i in range(N):
                pre_prod *= nums[i]
                if pre_prod > 0:
                    res = max(res, i + 1)
                elif first_neg == -1 and pre_prod < 0:
                    first_neg = i
                elif pre_prod < 0:
                    res = max(res, i - first_neg)
            return res
        num = []
        res = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                res = max(res, helper(num))
                num = []
            else:
                num.append(nums[i])
        res = max(res, helper(num))
        return res
