from collections import Counter
import heapq
class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        arrCount = Counter(arr)
        heap = []
        for num in arr:
            heapq.heappush(heap, (arrCount[num], num))
        
        while k > 0:
            num = heapq.heappop(heap)[1]
            arrCount[num] -= 1
            if arrCount[num] == 0:
                del arrCount[num]
            k-=1
        return len(arrCount)    
