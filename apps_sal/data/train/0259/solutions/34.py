class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        nums.sort()
        n = len(nums)

        start, end = 1, nums[-1]
        while start < end:
            mid = (start + end) // 2
            j = n - 1
            s = n
            while j >= 0 and mid < nums[j]:
                s -= 1
                s += math.ceil(nums[j] / mid)
                j -= 1
            if s > threshold:
                start = mid + 1
            else:
                end = mid
        return start
