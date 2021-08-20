class Solution:

    def longestSubarray(self, nums, limit):
        (max_h, min_h) = ([], [])
        res = l = 0
        for (r, num) in enumerate(nums):
            heapq.heappush(max_h, (-num, r))
            heapq.heappush(min_h, (num, r))
            while -max_h[0][0] - min_h[0][0] > limit:
                l += 1
                while max_h[0][1] < l:
                    heapq.heappop(max_h)
                while min_h[0][1] < l:
                    heapq.heappop(min_h)
            res = max(res, r - l + 1)
        return res
