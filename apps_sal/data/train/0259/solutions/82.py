class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:

        def calculate(divisor):
            _sum = 0
            for val in nums:
                _sum += val // divisor + int(val % divisor != 0)
            return _sum

        start, end = 1, max(nums)
        while start < end:
            mid = start + (end - start) // 2
            _sum = calculate(mid)
            if _sum > threshold:
                start = mid + 1
            else:
                end = mid
        return start
