class Solution:

    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        l = 1
        r = max(nums)
        while l < r:
            m = l + (r - l) // 2
            s = sum([ceil(x / m) for x in nums])
            if s > threshold:
                l = m + 1
            else:
                r = m
        return l
