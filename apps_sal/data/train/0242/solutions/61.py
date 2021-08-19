from collections import defaultdict


class Solution:

    def maxEqualFreq(self, nums: List[int]) -> int:
        if not nums:
            return 0
        (counter, freq) = (defaultdict(int), defaultdict(int))
        (max_f, ans) = (0, 0)
        for (idx, num) in enumerate(nums):
            counter[num] += 1
            max_f = max(max_f, counter[num])
            freq[counter[num] - 1] -= 1
            freq[counter[num]] += 1
            if max_f == 1 or max_f * freq[max_f] == idx or (max_f - 1) * (freq[max_f - 1] + 1) == idx:
                ans = idx + 1
        return ans
