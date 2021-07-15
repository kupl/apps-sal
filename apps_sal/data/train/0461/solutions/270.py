from collections import defaultdict
from collections import deque
class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        
        eg = defaultdict(set)
        mgr = None
        for i,man in enumerate(manager):
            if man != -1:
                eg[man].add(i)
            else:
                mgr = i
        # print(eg)
        time_map = {}
        for i, time in enumerate(informTime):
            time_map[i] = time
#         we are looking for the max path length when a leaf node is reached
        q = deque()
        q.append((mgr, time_map[mgr]))
        # print(time_map, q)
        max_it = -float('inf')
        
        while q:
            node, dist = q.popleft()
            # print(dist)
            if len(eg[node]) == 0:
                max_it = max(max_it, dist)
            
            for neighbor in eg[node]:
                q.append((neighbor, dist+time_map[neighbor]))
        
        return max_it
        

