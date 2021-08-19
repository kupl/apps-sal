import heapq


class Solution:

    def maxSubarraySumCircular(self, A: List[int]) -> int:
        N = len(A)
        best = A[0]
        heap = [(0, 0)]
        cumsums = [0]
        for n in A:
            cumsums.append(cumsums[-1] + n)
        for n in A:
            cumsums.append(cumsums[-1] + n)
        for i in range(1, len(cumsums)):
            while len(heap) > 0 and i - heap[0][1] > N:
                heapq.heappop(heap)
            best = max(best, cumsums[i] - heap[0][0])
            heapq.heappush(heap, (cumsums[i], i))
        return best
