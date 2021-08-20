import heapq


class Solution:

    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        heap = []
        for (k, v) in enumerate(nums):
            heapq.heappush(heap, [v, k])
        heapq.heapify(heap)
        ans = 0
        for i in range(1, right + 1):
            if len(heap) == 0:
                break
            (sum_v, index) = heapq.heappop(heap)
            if i >= left:
                ans = (ans + sum_v) % (10 ** 9 + 7)
            if index + 1 < n:
                heapq.heappush(heap, [sum_v + nums[index + 1], index + 1])
        return ans
