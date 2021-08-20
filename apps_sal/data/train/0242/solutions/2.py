class Solution:

    def maxEqualFreq(self, nums: List[int]) -> int:
        count = collections.defaultdict(int)
        freq = collections.defaultdict(int)
        for n in nums:
            count[n] += 1
            freq[count[n]] += 1
        for i in range(len(nums) - 1, 0, -1):
            if count[nums[i]] * freq[count[nums[i]]] == i:
                return i + 1
            freq[count[nums[i]]] -= 1
            count[nums[i]] -= 1
            if count[nums[i - 1]] * freq[count[nums[i - 1]]] == i:
                return i + 1
        return 1
