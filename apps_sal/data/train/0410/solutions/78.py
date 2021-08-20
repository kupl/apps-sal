class Solution:

    def getKth(self, lo: int, hi: int, k: int) -> int:

        def power(num):
            res = 0
            while num != 1:
                if num % 2 == 0:
                    num = num / 2
                else:
                    num = 3 * num + 1
                res += 1
            return res
        heap = []
        for i in range(lo, hi + 1):
            heap.append((power(i), i))
        heapq.heapify(heap)
        for i in range(k - 1):
            heapq.heappop(heap)
        return heap[0][1]
