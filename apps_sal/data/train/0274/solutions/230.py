from collections import deque


class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        minq = deque()
        maxq = deque()
        ret = l = 0
        for i in range(len(nums)):
            while minq and nums[i] < minq[-1]:
                minq.pop()
            minq.append(nums[i])
            while maxq and nums[i] > maxq[-1]:
                maxq.pop()
            maxq.append(nums[i])
            while maxq[0] - minq[0] > limit:
                if nums[l] == maxq[0]:
                    maxq.popleft()
                if nums[l] == minq[0]:
                    minq.popleft()
                l += 1
            ret = max(ret, i - l + 1)
        return ret
