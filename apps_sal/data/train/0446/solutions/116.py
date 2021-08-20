import heapq


class Solution:

    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        heap = []
        counter = collections.Counter()
        for num in arr:
            counter[num] = counter[num] + 1
        for (num, cnt) in counter.items():
            heapq.heappush(heap, (cnt, num))
        while k > 0:
            top = heapq.heappop(heap)
            if k >= top[0]:
                k -= top[0]
            else:
                heapq.heappush(heap, top)
                k = 0
        return len(heap)
