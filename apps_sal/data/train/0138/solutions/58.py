class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        n = len(nums)
        res = 0
        prod = 1
        p_start = -1
        n_start = 10 ** 6
        for i in range(n):
            if nums[i] == 0:
                p_start = i
                n_start = 10 ** 6
                prod = 1
                continue
            elif nums[i] < 0:
                prod = -prod
                if n_start == 10 ** 6:
                    n_start = i
            res = max(res, i - p_start) if prod > 0 else max(res, i - n_start)
        return res
