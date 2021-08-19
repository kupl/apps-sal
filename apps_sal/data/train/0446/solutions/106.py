class Solution:

    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        counter = collections.Counter(arr)
        import heapq
        heap = []
        for key in counter:
            heapq.heappush(heap, (counter[key], key))
        while heap and k:
            (count, key) = heapq.heappop(heap)
            if k >= count:
                k -= count
            else:
                return len(heap) + 1
        return len(heap)
