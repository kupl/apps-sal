class Solution:

    def longestSubarray(self, nums: List[int], limit: int) -> int:
        from sortedcontainers import SortedList
        wd = SortedList([nums[0]])
        max_len = 1
        l = 0
        r = 0
        while r < len(nums):
            minn = wd[0]
            maxx = wd[-1]
            if maxx - minn <= limit:
                max_len = max(max_len, r - l + 1)
                r += 1
                if r < len(nums):
                    wd.add(nums[r])
            else:
                wd.discard(nums[l])
                l += 1
        return max_len
