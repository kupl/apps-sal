from collections import Counter


class Solution:
    def maxEqualFreq(self, nums: List[int]) -> int:
        counts, freq = Counter(), Counter()
        ans, maxF = 0, 0
        for i, num in enumerate(nums):
            counts[num] += 1
            freq[counts[num] - 1] -= 1
            freq[counts[num]] += 1
            maxF = max(maxF, counts[num])
            if maxF * freq[maxF] == i or (maxF - 1) * (freq[maxF - 1] + 1) == i or maxF == 1:
                ans = i + 1
        return ans
