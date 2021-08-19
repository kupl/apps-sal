class Solution:
    import heapq

    def largestSumAfterKNegations(self, A: List[int], K: int) -> int:

        # find the min element and its index and negate it K times

        ## Complexity = O(kn)

        #         def findMin(A):
        #             minValue = float('inf')
        #             minIndex = 0

        #             for i, ele in enumerate(A):
        #                 if ele < minValue:
        #                     minValue = ele
        #                     minIndex = i

        #             return minIndex

        #         for k in range(K):
        #             minIndex = findMin(A)
        #             A[minIndex] = -A[minIndex]

        # using min heap

        heapq.heapify(A)
        for k in range(K):
            A[0] = -A[0]
            heapq.heapify(A)

        return sum(A)

    # let's do with heap, no need to pop just negate that element
