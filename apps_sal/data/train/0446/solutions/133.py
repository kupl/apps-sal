import heapq
from collections import defaultdict
class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        heap = []
        dic = defaultdict(int)
        for i in arr:
            dic[i] += 1
        for i in dic:
            heapq.heappush(heap, (dic[i], i))
        print(heap)
        while k:
            top = heap[0]
            if top[0] > k:
                break
            else:
                k -= top[0]
                heapq.heappop(heap)
        return len(heap)

