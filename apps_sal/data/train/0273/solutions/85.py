from collections import *

class Solution:
    def racecar(self, t: int) -> int:
        q, s, lvl = deque([(0, 1)]), set([(0, 1)]), 0
        
        while q:
            for _ in range(len(q)):
                pu, su = q.popleft()
                
                if pu == t:
                    return lvl
            
                a, r = (pu + su, su * 2), (pu, -1 if su > 0 else 1)
                for e in (a, r):
                    
                    if e in s or  e[0] < 0 or e[0] >= t * 2:
                        continue
                    q.append(e)
                    s.add(e)
            lvl += 1
            
        return 0

