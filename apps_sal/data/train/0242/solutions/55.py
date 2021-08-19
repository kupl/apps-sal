class Solution:

    def maxEqualFreq(self, nums: List[int]) -> int:
        (cnt, freq, maxF, res) = (collections.defaultdict(int), collections.defaultdict(int), 0, 0)
        for (i, num) in enumerate(nums):
            cnt[num] += 1
            freq[cnt[num] - 1] -= 1
            freq[cnt[num]] += 1
            maxF = max(maxF, cnt[num])
            if maxF * freq[maxF] == i or (maxF - 1) * (freq[maxF - 1] + 1) == i or maxF == 1:
                res = i + 1
        return res
