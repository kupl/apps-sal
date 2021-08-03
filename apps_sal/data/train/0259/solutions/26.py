class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        def check(nums, a, th):
            for n in nums:
                th -= math.ceil(n / a)
                if th < 0:
                    return False
            return True
        l, r = 1, max(nums)
        while l < r:
            mid = (l + r) // 2
            if check(nums, mid, threshold):
                r = mid
            else:
                l = mid + 1
        return l
