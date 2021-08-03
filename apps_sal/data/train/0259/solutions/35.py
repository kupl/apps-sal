class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        def condition(arr, thr, div):
            res = 0
            for i in arr:
                res += math.ceil(i / div)
            return res <= thr

        l, r = 1, max(nums)
        while l < r:
            m = l + (r - l) // 2
            if condition(nums, threshold, m):
                r = m
            else:
                l = m + 1

        return l
