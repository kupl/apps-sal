class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        cnts = collections.Counter(arr)
        heap = [(v, k) for k, v in cnts.items()]
        heapq.heapify(heap)
        for _ in range(k):
            cnt, val = heapq.heappop(heap)
            cnt -= 1
            if cnt != 0:
                heapq.heappush(heap, (cnt, val))
        return len(heap)
