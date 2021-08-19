class Solution:

    def longestSubarray(self, nums: List[int], limit: int) -> int:
        min_h = [(nums[0], 0)]
        max_h = [(-nums[0], 0)]
        heapq.heapify(min_h)
        heapq.heapify(max_h)
        (max_v, min_v) = (nums[0], nums[0])
        (l, r) = (0, 0)
        res = 1
        while r < len(nums):
            if max_v - min_v <= limit:
                r += 1
                if r < len(nums):
                    heapq.heappush(min_h, (nums[r], r))
                    heapq.heappush(max_h, (-nums[r], r))
                    (max_v, min_v) = (-max_h[0][0], min_h[0][0])
            else:
                res = max(res, r - l)
                l += 1
                while min_h[0][1] < l:
                    heapq.heappop(min_h)
                while max_h[0][1] < l:
                    heapq.heappop(max_h)
            (max_v, min_v) = (-max_h[0][0], min_h[0][0])
        return max(res, r - l)
