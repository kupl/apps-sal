class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        def helper(nums, ans):
            return sum([(i + ans - 1) // ans for i in nums])

        l = 1
        r = max(nums)
        while l < r:
            mid = l + (r - l) // 2
            sumv = helper(nums, mid)
            if sumv <= threshold:
                r = mid
            else:
                l = mid + 1

        return l
