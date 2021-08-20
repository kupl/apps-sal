def add_to_max_heap(heap, value):
    heapq.heappush(heap, value)


def add_to_min_heap(heap, value):
    heapq.heappush(heap, value)


def get_max_val(heap):
    return heap[0][0]


def get_min_val(heap):
    return heap[0][0]


class Solution:

    def longestSubarray(self, nums: List[int], limit: int) -> int:
        l = 0
        r = 0
        ans = 0
        max_heap = []
        min_heap = []
        while l < len(nums) and r < len(nums):
            add_to_max_heap(max_heap, (-nums[r], r))
            add_to_min_heap(min_heap, (nums[r], r))
            max_val = -get_max_val(max_heap)
            min_val = get_min_val(min_heap)
            if abs(max_val - min_val) <= limit:
                ans = max(ans, r - l + 1)
                r += 1
            else:
                while min_heap and min_heap[0][1] < l + 1:
                    heapq.heappop(min_heap)
                while max_heap and max_heap[0][1] < l + 1:
                    heapq.heappop(max_heap)
                l += 1
        return ans
