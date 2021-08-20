from collections import deque


class Solution:

    def longestSubarray(self, nums, limit):
        (res, last) = (0, -1)
        (maxQ, minQ) = (deque(), deque())
        for (i, val) in enumerate(nums):
            while maxQ and nums[maxQ[0]] - val > limit:
                last = max(last, maxQ.popleft())
            while maxQ and val >= nums[maxQ[-1]]:
                maxQ.pop()
            maxQ.append(i)
            while minQ and val - nums[minQ[0]] > limit:
                last = max(last, minQ.popleft())
            while minQ and val <= nums[minQ[-1]]:
                minQ.pop()
            minQ.append(i)
            res = max(res, i - last)
        return res
