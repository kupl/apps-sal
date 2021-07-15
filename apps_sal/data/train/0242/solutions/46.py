class Solution:
    def maxEqualFreq(self, nums: List[int]) -> int:
        counts, freq = collections.Counter(), collections.Counter()
        res = 0
        for i, num in enumerate(nums):
        
            counts[num] += 1
           
            freq[counts[num]] += 1

            count = freq[counts[num]] * counts[num]
            if count == i + 1 and i != len(nums) - 1: 
                res = max(res, i + 2)
            elif count == i:
                res = max(res, i + 1)
        return res

