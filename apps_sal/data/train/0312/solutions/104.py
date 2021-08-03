class Solution:
    def shortestSubarray(self, A, K):
        from heapq import heappush, heapify, heappop
        heap = []
        length = float('inf')
        summation = 0
        heapify(heap)
        heappush(heap, [0, -1])
        for i, number in enumerate(A):
            summation += number
            difference = summation - K
            while heap and (heap[0][0] <= difference or i - heap[0][1] >= length):
                previous_summation, previous_index = heappop(heap)
                length = min(length, i - previous_index)
            heappush(heap, [summation, i])
        return length if length != float('inf') else -1
