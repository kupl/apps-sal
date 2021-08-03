class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        start = 1
        end = max(nums)

        while start + 1 < end:
            mid = (start + end) // 2
            result = self.satistfy(nums, mid)

            if result <= threshold:
                end = mid
            else:
                start = mid

        if self.satistfy(nums, start) <= threshold:
            return start
        return end

    def satistfy(self, nums, mid):
        return sum(list([math.ceil(x / mid) for x in nums]))
