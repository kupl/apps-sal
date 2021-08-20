import heapq


class Solution:

    def maxSubarraySumCircular(self, A: List[int]) -> int:
        N = len(A)
        best = A[0]
        heap = [(0, -1)]
        current_sum = 0
        for i in range(2 * N):
            current_sum += A[i % N]
            while len(heap) > 0 and i - heap[0][1] > N:
                heapq.heappop(heap)
            best = max(best, current_sum - heap[0][0])
            heapq.heappush(heap, (current_sum, i))
        return best
