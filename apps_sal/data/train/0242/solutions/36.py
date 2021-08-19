class Solution:

    def maxEqualFreq(self, nums: List[int]) -> int:
        count = collections.Counter()
        n = len(nums)
        freq = collections.Counter()
        res = 0
        for (i, a) in enumerate(nums, 1):
            if count[a] in freq:
                freq[count[a]] -= 1
            freq[count[a] + 1] += 1
            count[a] += 1
            f = count[a]
            if freq[f] * f == i and i < n:
                res = i + 1
            else:
                d = i - freq[f] * f
                if d in [1, f + 1] and freq[d] == 1:
                    res = i
        return res
