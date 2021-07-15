from sortedcontainers import SortedList
class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        s = SortedList()
        j = ans = 0
        for i, val in enumerate(nums):
            s.add(val)
            while s and s[-1] - s[0] > limit:
                s.remove(nums[j])
                j += 1
            ans = max(ans, (i - j + 1))
        return ans

