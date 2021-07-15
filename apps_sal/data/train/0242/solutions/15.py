class Solution:
    def maxEqualFreq(self, nums: List[int]) -> int:
        count = collections.Counter()
        freq = [0 for _ in range(len(nums) + 1)]
        res = 0
        for n, a in enumerate(nums, 1):
            freq[count[a]] -= 1
            freq[count[a] + 1] += 1
            c = count[a] = count[a] + 1
            if freq[c] * c == n and n < len(nums):
                res = n + 1
            d = n - freq[c] * c
            if d in [c + 1, 1] and freq[d] == 1:
                res = n
        return res
