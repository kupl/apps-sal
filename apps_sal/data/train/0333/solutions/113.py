from collections import defaultdict
from heapq import heappush, heappop

class Solution:
    def adjacent(self, arr, i, jumps):
        if i > 0:
            yield i - 1
        if i < len(arr) - 1:
            yield i + 1
        
        for j in jumps[arr[i]]:
            if i != j:
                yield j
        
    def minJumps(self, arr: List[int]) -> int:
        if not arr:
            return 0
        
        jumps = defaultdict(set)
        for i, v in enumerate(arr):
            if i == 0 or i == len(arr) - 1 or arr[i - 1] != v or arr[i + 1] != v:
                jumps[v].add(i)
        
        steps = {}
        
        pq = []
        heappush(pq, (0, 0))
        
        while pq:
            n, neg_i = heappop(pq)
            i = -neg_i
            
            if i == len(arr) - 1:
                return n
            
            for j in self.adjacent(arr, i, jumps):
                if j not in steps or steps[j] > n + 1:
                    steps[j] = n + 1
                    heappush(pq, (n + 1, -j))

