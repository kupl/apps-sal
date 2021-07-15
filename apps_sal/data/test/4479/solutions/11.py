class Solution:
    import heapq
    def largestSumAfterKNegations(self, A: List[int], K: int) -> int:
        heapq.heapify(A)
        for i in range(K):
            m = heapq.heappop(A)
            heapq.heappush(A, -m)
        return sum(A)

