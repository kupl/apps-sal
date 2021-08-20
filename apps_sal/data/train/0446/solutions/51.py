class Solution:

    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        d = {}
        for num in arr:
            try:
                d[num] += 1
            except:
                d[num] = 1
        heap = []
        for key in list(d.keys()):
            heapq.heappush(heap, (d[key], key))
        while k:
            popped = heapq.heappop(heap)
            key = popped[1]
            d[key] -= 1
            if not d[key]:
                del d[key]
            else:
                heapq.heappush(heap, (d[key], key))
            k -= 1
        return len(list(d.keys()))
