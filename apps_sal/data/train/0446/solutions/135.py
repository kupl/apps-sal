class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        heap = []
        for key, val in collections.Counter(arr).items():
            heapq.heappush(heap, (val, key))

        for _ in range(k):
            val, key = heapq.heappop(heap)
            #val -= 1
            if val > 1:
                heapq.heappush(heap, (val - 1, key))

        return len(heap)
