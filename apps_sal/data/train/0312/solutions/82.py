class Solution:
    def shortestSubarray(self, A: List[int], K: int) -> int:
        Sum, res, heap, flag = 0, len(A), [(0, -1)], False
        
        for i, v in enumerate(A):
            Sum += v
            while heap and Sum - heap[0][0] >= K:
                flag = True
                res = min(res, i - heapq.heappop(heap)[1])
            heapq.heappush(heap, (Sum, i))
        
        return res if flag else -1
            

