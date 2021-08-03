class Solution:
    #     def longestSubarray(self, nums: List[int], limit: int) -> int:
    #         min_h = [(nums[0], 0)]
    #         max_h = [(-nums[0], 0)]

    #         heapq.heapify(min_h)
    #         heapq.heapify(max_h)

    #         max_v, min_v = nums[0], nums[0]
    #         l, r = 0, 0
    #         res = 1
    #         while r < len(nums):
    #             if max_v - min_v <= limit:
    #                 r += 1
    #                 if r < len(nums):
    #                     heapq.heappush(min_h, (nums[r], r))
    #                     heapq.heappush(max_h, (-nums[r], r))
    #                     max_v, min_v = -max_h[0][0], min_h[0][0]
    #             else:
    #                 res = max(res, r-l)
    #                 l += 1
    #                 while min_h[0][1] < l:
    #                     heapq.heappop(min_h)
    #                 while max_h[0][1] < l:
    #                     heapq.heappop(max_h)
    #             max_v, min_v = -max_h[0][0], min_h[0][0]

    #         return max(res, r-l)

    def longestSubarray(self, nums, limit):
        max_h, min_h = [], []
        res = l = 0

        for r, num in enumerate(nums):
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
