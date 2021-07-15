class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        total_remainder = sum(nums) % p
        prev = {}
        res = len(nums)
        current_sum = 0
        prev[current_sum] = 0
        for i in range(len(nums)):
            current_sum = (current_sum + nums[i]) % p
            prev[current_sum] = i + 1
            other = (current_sum - total_remainder) % p
            if other in prev:
                res = min(res, i + 1 - prev[other])
        return res if res < len(nums) else -1
