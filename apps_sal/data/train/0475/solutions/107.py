import heapq


class Solution:

    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        heap = [(num, i) for (i, num) in enumerate(nums)]
        heapq.heapify(heap)
        res = 0
        for k in range(1, right + 1):
            (num, idx) = heapq.heappop(heap)
            if k >= left:
                res += num
            if idx + 1 < len(nums):
                heapq.heappush(heap, (num + nums[idx + 1], idx + 1))
        return res % (10 ** 9 + 7)
