from collections import deque
class Solution:
    def maxCandies(self, status: List[int], candies: List[int], keys: List[List[int]], containedBoxes: List[List[int]], initialBoxes: List[int]) -> int:
        
        q = deque(initialBoxes)
        visited = set()
        res = 0
        while q:
            itr, opened = len(q), False  # To detect cycle
            opened = False
            while (itr):
                itr -= 1
                v = q.popleft()
                if status[v]: # Open box, (key is available or is open)
                    
                    opened = True
                    res += candies[v]
                    visited.add(v)
                    
                    for x in keys[v]:
                        status[x] = 1
                    
                    for x in containedBoxes[v]:
                        if x not in visited:
                            q.append(x)
                            
                elif v not in visited: # Open when key is available
                    q.append(v)
            if not opened:
                return res  # Exit cycle detected
        return res

