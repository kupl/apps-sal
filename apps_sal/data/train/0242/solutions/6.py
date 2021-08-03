class Solution:
    def maxEqualFreq(self, nums: List[int]) -> int:
        counts = collections.defaultdict(int)
        freq = collections.defaultdict(int)
        res = 0
        for i in range(len(nums)):
            counts[nums[i]] += 1
            freq[counts[nums[i]]] += 1

            count = counts[nums[i]] * freq[counts[nums[i]]]
            if count == i + 1 and i != len(nums) - 1:
                res = max(res, i + 2)
            elif count == i:
                res = max(res, i + 1)
        return res
