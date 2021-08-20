class Solution:

    def largestSumAfterKNegations(self, A: List[int], K: int) -> int:
        heapq.heapify(A)
        for x in range(K):
            heapreplace(A, -A[0])
        return sum(A)
