class Solution:
    def largestSumAfterKNegations(self, A: List[int], K: int) -> int:
        heapq.heapify(A)
        # heapify is in place algo so take linear time
        for x in range(K):
            # if x %2 :
            #heappreplace(A, -A[0])
            #heappush(A, -heapq.heappop(A))
            heapreplace(A, -A[0])
        return sum(A)
