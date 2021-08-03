import heapq


class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        left -= 1
        right -= 1
        sums = [nums[0]]
        for i in range(1, n):
            sums.append(sums[i - 1] + nums[i])
        heap = [-e for e in sums]
        heapq.heapify(heap)
        size = right + 1
        while len(heap) > size:
            heapq.heappop(heap)
        for s in range(1, n):
            for e in range(s, n):
                v = sums[s - 1] - sums[e]
                if len(heap) < size or v >= heap[0]:
                    heapq.heappush(heap, v)
                if len(heap) > size:
                    heapq.heappop(heap)
        acc = 0
        for _ in range(right - left + 1):
            acc = (acc - heapq.heappop(heap)) % (10**9 + 7)
        return acc
