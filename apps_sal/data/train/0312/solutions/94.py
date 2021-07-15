import heapq
class Solution:
    def shortestSubarray(self, A: List[int], K: int) -> int:
        prefix = 0
        pq = [[0, -1]]
        res = float('inf')
        for i, a in enumerate(A):
            prefix += a
            while pq and prefix - pq[0][0] >= K:
                res = min(res, i - heapq.heappop(pq)[1])
            heapq.heappush(pq, [prefix, i])
        return res if res < float('inf') else -1
            
        
#         prefix = [0]
#         for a in A:
#             prefix.append(prefix[-1] + a)
#         res = float('inf')
#         deq = collections.deque()
        
        
#         prefix = [0]
#         for a in A:
#             prefix.append(prefix[-1] + a)
#         res = float('inf')
#         deq = collections.deque()
#         for i, x in enumerate(prefix):
#             while deq and prefix[deq[-1]] >= x:
#                 deq.pop()
#             while deq and prefix[deq[0]] <= x - K:
#                 res = min(res, i - deq.popleft())
#             deq.append(i)
#         return res if res < float('inf') else -1

