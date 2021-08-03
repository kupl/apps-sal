import bisect


class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:

        if len(nums) <= 1:
            return len(nums)

        h = [nums[0]]
        right, left, max_len = 0, 0, 1
        lo, hi = nums[0], nums[0]

        while right < len(nums) and left < len(nums):

            if abs(hi - lo) <= limit:

                max_len = max(max_len, right - left + 1)

                right += 1
                if right < len(nums):
                    hi = max(nums[right], hi)
                    lo = min(nums[right], lo)
                    bisect.insort(h, nums[right])
            else:
                del h[bisect.bisect_left(h, nums[left])]
                lo, hi = h[0], h[-1]
                left += 1

        return max_len
