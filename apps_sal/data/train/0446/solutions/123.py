class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        
        freqs = collections.Counter(arr)
        #{1: 2 , 2:1 , 3:3, 4:1}
        
        heap = []
        
        for key, val in list(freqs.items()):
            heapq.heappush(heap, [val, key])
            
        while k > 0:
            heap[0][0] -= 1
            if heap[0][0] == 0:
                heapq.heappop(heap)
            k -= 1
        
        return len(heap)
            

