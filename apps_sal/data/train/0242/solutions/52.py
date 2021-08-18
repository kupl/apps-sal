class Solution:
    def maxEqualFreq(self, nums: List[int]) -> int:
        freq = collections.Counter()
        counts = collections.Counter()
        res = 0
        for i, val in enumerate(nums):
            save = freq[val]
            if save:
                counts[save] -= 1
                if not counts[save]:
                    del counts[save]
            freq[val] += 1
            counts[freq[val]] += 1
            if len(counts) == 1 and (counts[1] > 0 or len(freq) == 1):
                res = i + 1
            if len(counts) == 2:
                (a, b) = list(counts.keys())
                if abs(a - b) == 1 and counts[max(a, b)] == 1:
                    res = i + 1
                if counts[1] == 1:
                    res = i + 1
        return res
