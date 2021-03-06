class Solution:

    def longestSubarray(self, nums: List[int], limit: int) -> int:
        (max_heap, min_heap) = ([], [])
        max_len = 0
        l = 0
        for (r, n) in enumerate(nums):
            heapq.heappush(max_heap, (-n, r))
            heapq.heappush(min_heap, (n, r))
            while -max_heap[0][0] - min_heap[0][0] > limit:
                l = min(max_heap[0][1], min_heap[0][1]) + 1
                while max_heap[0][1] < l:
                    heapq.heappop(max_heap)
                while min_heap[0][1] < l:
                    heapq.heappop(min_heap)
            max_len = max(max_len, r - l + 1)
        return max_len
        '\n        # using heaps\n        maxq, minq = [], []\n        n = len(nums)\n        \n        r = 0\n        for l in range(n):\n            heapq.heappush(maxq, (-nums[i], l))\n            heapq.heappush(minq, (nums[i], l))\n            \n            \n            while abs(maxq[0][0] + minq[0][0]) <= limit:\n                while max[0][0]\n        '
