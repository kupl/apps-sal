class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        start = 1
        end = max(nums)

        while start + 1 < end:
            mid = (start + end) // 2
            result = sum(list([math.ceil(x / mid) for x in nums]))

            if result <= threshold:
                end = mid
            else:
                start = mid

        if sum(list([math.ceil(x / start) for x in nums])) <= threshold:
            return start
        return end
