class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        from collections import Counter
        from heapq import heapify, heappop
        heap = [(val, key) for key, val in list(Counter(arr).items())]
        heapify(heap)
        while k > 0:
            k -= heappop(heap)[0]
        return len(heap) + (k < 0)
