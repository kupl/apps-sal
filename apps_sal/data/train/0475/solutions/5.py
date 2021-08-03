class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        heap = []
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = nums[i] + prefix[i]
        for i in range(n):
            for j in range(i + 1, n + 1):
                heapq.heappush(heap, prefix[j] - prefix[i])
        res = 0
        for i in range(left - 1):
            heapq.heappop(heap)
        for i in range(right - left + 1):
            res = (res + heapq.heappop(heap)) % (10**9 + 7)
        return res
