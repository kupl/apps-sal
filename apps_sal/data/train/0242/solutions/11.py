class Solution:
    def maxEqualFreq(self, nums: List[int]) -> int:
        from collections import defaultdict
        freq = defaultdict(int)
        count = defaultdict(int)
        res = 0
        for i, n in enumerate(nums, 1):
            freq[count[n]] -= 1
            freq[count[n] + 1] += 1
            count[n] += 1

            if freq[count[n]] * count[n] == i and i < len(nums):
                res = i + 1

            d = i - freq[count[n]] * count[n]
            if d in [1, count[n] + 1] and freq[d] == 1:
                res = i
        return res
