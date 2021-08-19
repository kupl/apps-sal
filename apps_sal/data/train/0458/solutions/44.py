class Solution:

    def minSubarray(self, nums: List[int], p: int) -> int:
        need = sum(nums) % p
        cum_sum = 0
        if need == 0:
            return 0
        d = {}
        d[0] = -1
        min_len = len(nums)
        for (i, num) in enumerate(nums):
            cum_sum = (cum_sum + num) % p
            if (cum_sum - need) % p in d:
                min_len = min(min_len, i - d[(cum_sum - need) % p])
            d[cum_sum] = i
        return -1 if min_len == len(nums) else min_len
