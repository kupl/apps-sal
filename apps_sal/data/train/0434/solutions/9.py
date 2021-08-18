class Solution:
    def longestSubarray(self, nums: List[int]) -> int:

        noofones = 0
        m = 0
        lastoneslen = 0

        for i in nums:
            if i == 1:
                noofones += 1
            else:
                m = max(m, noofones + lastoneslen)
                lastoneslen = noofones
                noofones = 0

        m = max(m, noofones + lastoneslen)

        if m == len(nums):
            m -= 1

        return m
