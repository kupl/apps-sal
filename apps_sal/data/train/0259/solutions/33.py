class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        l, r = 1, max(nums)
        count = 0
        while l < r:
            m = l + (r-l)//2
            for i in nums:
                count += (i + m -1) // m
            if count > threshold:
                l = m + 1
            else:
                r = m
            count = 0
        return l
        

