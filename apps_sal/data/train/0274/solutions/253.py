class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        from collections import deque
        asc, desc = deque(), deque()
        l, r = 0, 0
        res = 0
        while r < len(nums):
            while asc and nums[asc[-1]] >= nums[r]: asc.pop()
            while desc and nums[desc[-1]] <= nums[r]: desc.pop()
            asc.append(r)
            desc.append(r)
            while nums[desc[0]] - nums[asc[0]] > limit:
                l += 1
                if desc[0] < l: desc.popleft()
                if asc[0] < l: asc.popleft()
            res = max(res, r - l + 1)
            r += 1
        return res
