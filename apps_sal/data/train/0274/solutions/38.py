# can get a o(n logn runtime)
# use min and max heaps

from heapq import *
from collections import Counter


class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:

        min_heap = []
        max_heap = []

        lazy_delete_min_heap = Counter()
        lazy_delete_max_heap = Counter()

        l = 0
        longest = 0
        for r in range(len(nums)):
            heappush(min_heap, nums[r])
            heappush(max_heap, -nums[r])

            while abs(nums[r] - min_heap[0]) > limit or abs(nums[r] + max_heap[0]) > limit:

                lazy_delete_min_heap[nums[l]] += 1
                lazy_delete_max_heap[nums[l]] += 1

                while lazy_delete_min_heap[min_heap[0]] > 0:
                    lazy_delete_min_heap[min_heap[0]] -= 1
                    heappop(min_heap)

                while lazy_delete_max_heap[-max_heap[0]] > 0:
                    lazy_delete_max_heap[-max_heap[0]] -= 1
                    heappop(max_heap)

                l += 1

            longest = max(longest, r - l + 1)

        return longest
