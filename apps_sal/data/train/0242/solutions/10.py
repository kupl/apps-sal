from collections import defaultdict


class Solution:

    def maxEqualFreq(self, nums: List[int]) -> int:
        if not nums:
            return 0
        ans = 0
        max_f = 0
        (counter, freq_counter) = (defaultdict(int), defaultdict(int))
        for (idx, val) in enumerate(nums):
            counter[val] += 1
            max_f = max(max_f, counter[val])
            freq_counter[counter[val] - 1] -= 1
            freq_counter[counter[val]] += 1
            if max_f == 1 or max_f * freq_counter[max_f] == idx or (max_f - 1) * (freq_counter[max_f - 1] + 1) == idx:
                ans = max(ans, idx + 1)
        return ans
