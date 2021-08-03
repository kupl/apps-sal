class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        l = 1
        u = max(nums)

        def division_sum(k):
            return sum(int(math.ceil(n / k)) for n in nums)

        while l < u:
            mid = l + (u - l) // 2

            if division_sum(mid) <= threshold:
                u = mid
            else:
                l = mid + 1

        return l
