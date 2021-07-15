from functools import lru_cache
from heapq import heappop, heappush

class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        
        @lru_cache(None)
        def get_steps(num):
            if num == 1:
                return 0
            elif num % 2:
                return 1 + get_steps(3 * num + 1)
            else:
                return 1 + get_steps(num // 2)
            
        pq = []
        for i in range(lo, hi + 1):
            heappush(pq, (-get_steps(i), -i))
            if len(pq) > k:
                heappop(pq)
        
        return -min(pq)[1]
