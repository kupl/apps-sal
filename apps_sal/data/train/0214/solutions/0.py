class Solution:
    def movesToMakeZigzag(self, nums):
        n = len(nums)
        res0 = 0
        for i in range(0, n, 2):
            nei = min(nums[j] for j in [i - 1, i + 1] if 0 <= j <= n-1)
            if nums[i] >= nei:
                res0 += nums[i] - nei + 1
        res1 = 0
        for i in range(1, n, 2):
            nei = min(nums[j] for j in [i - 1, i + 1] if 0 <= j <= n-1)
            if nums[i] >= nei:
                res1 += nums[i] - nei + 1
        return min(res0, res1)
