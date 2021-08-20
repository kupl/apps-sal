class Solution:

    def longestSubarray(self, nums: List[int], limit: int) -> int:
        n = len(nums)
        (i, j, ans) = (0, 0, 0)
        (min_heap, max_heap) = ([], [])
        heapq.heapify(min_heap)
        heapq.heapify(max_heap)
        while i <= j < n:
            heapq.heappush(min_heap, (nums[j], j))
            heapq.heappush(max_heap, (-nums[j], j))
            while i <= j < n and -max_heap[0][0] - min_heap[0][0] > limit:
                i += 1
                while min_heap and min_heap[0][1] < i:
                    heapq.heappop(min_heap)
                while max_heap and max_heap[0][1] < i:
                    heapq.heappop(max_heap)
            ans = max(ans, j - i + 1)
            j += 1
        return ans
