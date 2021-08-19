from collections import defaultdict


class Solution:

    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        seen = defaultdict(int)
        seen[0] = 1
        output = 0
        odds = 0
        for i in range(0, len(nums)):
            if nums[i] % 2 != 0:
                odds += 1
            if odds - k in seen:
                output += seen[odds - k]
            seen[odds] += 1
        return output
