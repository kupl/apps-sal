from collections import defaultdict
class Solution:
    def maxEqualFreq(self, nums: List[int]) -> int:
        counter, freq = defaultdict(int), defaultdict(int)
        max_f = 0
        ans = 0
        for idx, num in enumerate(nums):
            counter[num] += 1
            freq[counter[num]-1] -= 1
            freq[counter[num]] += 1
            max_f = max(max_f, counter[num])
            if freq[max_f] * max_f == idx or max_f == 1 or (max_f-1)*(freq[max_f-1] + 1) == idx:
                ans = idx+1
        return ans
