class Solution:

    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        heap = []
        for (key, val) in list(collections.Counter(arr).items()):
            heapq.heappush(heap, (val, key))
        while k > 0:
            (val, key) = heapq.heappop(heap)
            if val > k:
                heapq.heappush(heap, (val - k, key))
                break
            else:
                k -= val
        return len(heap)
