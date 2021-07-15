class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        heap = []
        dic = collections.Counter(arr)
        for element, count in list(dic.items()):
            heapq.heappush(heap, [count, element])
        while k > 0:
            count, element = heapq.heappop(heap)
            if count > 1:
                heapq.heappush(heap, [count-1,element])
            k-=1
        return len(heap)

