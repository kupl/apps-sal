from collections import defaultdict


class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        if len(nums) < k:
            return 0

        # Cummulative count of number of odds
        num_odd = 0
        # Store number of sub-arrays with count [key] previously seen
        seen = defaultdict(int)
        seen[0] = 1  # Empty subarray has 0 odd numbers

        ret = 0
        for i in range(len(nums)):
            if nums[i] % 2 == 1:
                num_odd += 1
            key = num_odd - k
            ret += seen[key]
            seen[num_odd] += 1
        return ret
