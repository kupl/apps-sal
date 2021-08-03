from heapq import heappush, heappop


class Solution:
    def longestSubarray(self, nums, limit):
        discard = -1
        res = 0
        minq, maxq = [], []

        for i in range(len(nums)):
            while (minq and abs(nums[i] - minq[0][0]) > limit):
                _, index = heappop(minq)
                discard = max(discard, index)
            heappush(minq, (nums[i], i))
            while (maxq and abs(nums[i] + maxq[0][0]) > limit):
                _, index = heappop(maxq)
                discard = max(discard, index)
            heappush(maxq, (-nums[i], i))

            res = max(res, i - discard)

        return res
