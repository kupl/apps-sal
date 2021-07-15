class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        heap = []
        counts = collections.Counter()
        for num in arr:
            counts[num] += 1
        
        for num,cnt in counts.items():
            heapq.heappush(heap, (cnt, num))
            
        while k > 0:
            top = heapq.heappop(heap)
            if k >= top[0]:
                k -= top[0]
            else:
                heapq.heappush(heap, top)
                k = 0
        return len(heap)
