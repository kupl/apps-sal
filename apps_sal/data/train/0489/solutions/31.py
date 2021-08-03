class Solution:
    def maxWidthRamp(self, A: List[int]) -> int:
        minHeap = [(A[i], i) for i in range(len(A))]
        heapq.heapify(minHeap)
        maxWidth = 0
        minVal, minPos = heapq.heappop(minHeap)

        while minHeap:
            val, pos = heapq.heappop(minHeap)
            if val >= minVal:
                maxWidth = max(maxWidth, pos - minPos)
            if pos < minPos:
                minVal = val
                minPos = pos

        return maxWidth
