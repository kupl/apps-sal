class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        total_remainder = 0
        for num in nums:
            total_remainder = (total_remainder + num) % p
        prev = {}
        res = len(nums)
        current_sum = 0
        prev[current_sum] = 0
        for i, num in enumerate(nums):
            current_sum = (current_sum + num) % p
            prev[current_sum] = i + 1
            other = (current_sum - total_remainder + p) % p
            if other in prev:
                res = min(res, i + 1 - prev[other])
        return res if res < len(nums) else -1
