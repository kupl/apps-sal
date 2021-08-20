from collections import deque


class Solution:

    def longestSubarray(self, nums: List[int], limit: int) -> int:
        lo = i = ans = 0
        (minq, maxq) = (deque(), deque())
        while i < len(nums):
            while minq and minq[-1][1] >= nums[i]:
                minq.pop()
            while maxq and maxq[-1][1] <= nums[i]:
                maxq.pop()
            minq.append((i, nums[i]))
            maxq.append((i, nums[i]))
            if maxq[0][1] - minq[0][1] > limit:
                lo += 1
                if lo > minq[0][0]:
                    minq.popleft()
                if lo > maxq[0][0]:
                    maxq.popleft()
            else:
                ans = max(ans, i - lo + 1)
                i += 1
        return ans
