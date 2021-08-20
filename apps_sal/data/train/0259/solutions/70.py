class Solution:

    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        left = 1
        right = max(nums)
        while left < right:
            mid = (left + right) // 2
            cur_sum = 0
            for each in nums:
                cur_sum += math.ceil(each / mid)
            if cur_sum <= threshold:
                right = mid
            else:
                left = mid + 1
        return left
