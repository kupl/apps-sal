class Solution:

    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        heap = []
        for i in range(n):
            heap.append((nums[i], i))
        heapify(heap)
        res = 0
        for i in range(1, right + 1):
            (s, r) = heappop(heap)
            if i >= left:
                res += s
            if r + 1 < n:
                heappush(heap, (s + nums[r + 1], r + 1))
        return res % 1000000007
