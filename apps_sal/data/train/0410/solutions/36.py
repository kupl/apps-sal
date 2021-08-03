class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        heap = []
        for i in range(lo, hi + 1):
            ret = i
            steps = 0
            while ret != 1:
                if ret % 2 == 0:
                    ret = ret // 2
                else:
                    ret = 3 * ret + 1
                steps += 1

            heapq.heappush(heap, (-steps, -i))
            if len(heap) > k:
                heapq.heappop(heap)
        return -(heap[0][1])
