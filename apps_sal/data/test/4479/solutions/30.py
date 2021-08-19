class Solution:
    import heapq

    def largestSumAfterKNegations(self, A: List[int], K: int) -> int:
        heapq.heapify(A)
        for k in range(K):
            A[0] = -A[0]
            heapq.heapify(A)
        return sum(A)
