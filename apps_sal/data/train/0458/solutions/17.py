class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        total_divisor = sum(nums) % p
        if total_divisor == 0:
            return 0
        last_position = collections.defaultdict(lambda: -math.inf)
        last_position[0] = -1
        res = len(nums)
        cur_sum = 0
        for i, num in enumerate(nums):
            cur_sum += num
            res = min(res, i - last_position[(cur_sum - total_divisor) % p])
            last_position[cur_sum % p] = i
        if res == len(nums):
            return -1
        else:
            return res
