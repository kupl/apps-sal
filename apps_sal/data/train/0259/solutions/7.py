class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        l, r = 1, max(nums)
        while l < r:
            m = (l + r) // 2
            sum_num = 0
            for i in nums:
                sum_num += (i + m - 1) // m
            if sum_num > threshold:
                l = m + 1
            else:
                r = m
        return l
