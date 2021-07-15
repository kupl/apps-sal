class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        if len(nums) < 2:
            return 1
        longestSize = 1
        left = 0
        lo_q, hi_q = [], []
        heapq.heappush(lo_q, (nums[0], 0))
        heapq.heappush(hi_q, (-nums[0], 0))
        for idx in range(1, len(nums)):
            if lo_q and nums[idx] < lo_q[0][0]:
                lo_q = []
            elif hi_q and -nums[idx] < hi_q[0][0]:
                hi_q = []
            heapq.heappush(lo_q, (nums[idx], idx))
            heapq.heappush(hi_q, (-nums[idx], idx))

            while lo_q and abs(nums[idx] - lo_q[0][0]) > limit:
                left = max(left, heapq.heappop(lo_q)[1] + 1)
            while hi_q and abs(nums[idx] + hi_q[0][0]) > limit:
                left = max(left, heapq.heappop(hi_q)[1] + 1)
            longestSize = max(longestSize, idx - left + 1)
        return longestSize
