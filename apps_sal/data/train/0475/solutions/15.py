class Solution:

    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        n = len(nums)
        heap = [(x, i) for (i, x) in enumerate(nums)]
        heapq.heapify(heap)
        res = 0
        for j in range(1, right + 1):
            (x, i) = heapq.heappop(heap)
            if j >= left:
                res += x
            if i + 1 < n:
                heapq.heappush(heap, (x + nums[i + 1], i + 1))
        return res % (10 ** 9 + 7)
