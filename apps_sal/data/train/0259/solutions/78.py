class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        l = 1
        r = max(nums)

        def helper(arr, mid, threshold):
            return sum([math.ceil(num / mid) for num in arr]) <= threshold

        while l <= r:
            mid = (l + r) // 2
            if helper(nums, mid, threshold):
                r = mid - 1
            else:
                l = mid + 1
        return l
