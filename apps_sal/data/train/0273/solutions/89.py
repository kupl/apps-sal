from collections import deque
class Solution:
    def racecar(self, target: int) -> int:
        visited = set()
        
        q = deque([(0,1,0)])
        while q:
            pos, sp, d = q.popleft()
            #print(pos, q)
            if pos==target:
                return d

            if (pos, sp) in visited:
                continue
            visited.add((pos, sp))
            
            if abs(sp)>target or pos<0:
                # in these cases, must turn.
                q.append((pos, -1*(sp//abs(sp)), d+1))
            else:
                # can keep goint or turn.
                q.append((pos+sp, sp*2, d+1))
                q.append((pos, -1*(sp//abs(sp)), d+1))

