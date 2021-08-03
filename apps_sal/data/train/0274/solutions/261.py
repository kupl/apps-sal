from collections import deque


class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        if not nums:
            return 0

        minq, maxq = deque(), deque()
        l = r = 0
        ans = 0
        while r < len(nums):
            while minq and nums[r] <= nums[minq[-1]]:
                minq.pop()
            while maxq and nums[r] >= nums[maxq[-1]]:
                maxq.pop()

            minq.append(r)
            maxq.append(r)

            while nums[maxq[0]] - nums[minq[0]] > limit:
                l += 1
                if l > minq[0]:
                    minq.popleft()
                if l > maxq[0]:
                    maxq.popleft()
            ans = max(ans, r - l + 1)
            r += 1
        return ans
