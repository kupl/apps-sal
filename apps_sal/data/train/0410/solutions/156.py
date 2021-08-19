class Solution:

    def powerValue(self, n):
        count = 0
        while n != 1:
            if n % 2 == 0:
                n = n / 2
            else:
                n = 3 * n + 1
            count += 1
        return count

    def getKth(self, lo: int, hi: int, k: int) -> int:
        minHeap = []
        for i in range(lo, hi + 1):
            heapq.heappush(minHeap, (self.powerValue(i), i))
        i = 1
        while i < k:
            heapq.heappop(minHeap)
            i += 1
        return minHeap[0][1]
