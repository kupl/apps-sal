import heapq


class Solution:

    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        counter = collections.Counter(arr)
        heap = [(value, key) for (key, value) in list(counter.items())]
        heapq.heapify(heap)
        while k > 0:
            k -= heapq.heappop(heap)[0]
        return len(heap) + (k < 0)
