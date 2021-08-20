class Solution:

    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        freqm = collections.defaultdict(int)
        for a in arr:
            freqm[a] += 1
        heap = []
        for (key, val) in freqm.items():
            heapq.heappush(heap, (val, key))
        totalKeys = len(heap)
        count = 0
        while k > 0 and heap:
            (val, key) = heapq.heappop(heap)
            if k >= val:
                k -= val
                count += 1
            else:
                break
        return totalKeys - count
