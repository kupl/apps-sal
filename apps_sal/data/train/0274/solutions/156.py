from typing import List
from sortedcontainers import SortedList


class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        i, j = 0, 0
        maxLen = 1
        sortedInterval = SortedList([nums[0]])

        while i <= j < len(nums):
            minVal, maxVal = sortedInterval[0], sortedInterval[-1]
            if maxVal - minVal <= limit:
                maxLen = max(j - i + 1, maxLen)
                j += 1
                if j < len(nums):
                    sortedInterval.add(nums[j])
            elif i < j:
                sortedInterval.discard(nums[i])
                i += 1
            else:
                j += 1
                i = j

        return maxLen

