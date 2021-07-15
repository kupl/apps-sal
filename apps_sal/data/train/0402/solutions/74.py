class Solution:
    def isEscapePossible(self, blocked: List[List[int]], source: List[int], target: List[int]) -> bool:
        blocked = {tuple(p) for p in blocked}
        direction = [[0,1],[0,-1],[1,0],[-1,0]]
        
        def bfs(source, target):
            bfs, seen = [source], {tuple(source)}
            
            for x0, y0 in bfs:
                for i, j in direction:
                    x, y = x0 + i, y0 + j
                    if 0 <= x < 10**6 and 0 <= y < 10**6 and (x, y) not in seen and (x, y) not in blocked:
                        if [x, y] == target: 
                            return True
                        
                        bfs.append([x, y])
                        seen.add((x, y))
                        
                if len(bfs) == 20000: 
                    return True
                
            return False
        
        return bfs(source, target) and bfs(target, source)
    
    
class Solution_:
    def isEscapePossible_(self, blocked: List[List[int]], source: List[int], target: List[int]) -> bool:
        
        queue = collections.deque()
        direction = [[0,1],[0,-1],[1,0],[-1,0]]
        
        queue.append(source)
        
        s = set()
        for i,j in blocked:
            s.add((i,j))
  
        while queue:
            x, y = queue.popleft()
            
            if [x,y] == target:
                return True
            
            for xx, yy in direction:
                if x+xx >= 0 and x+xx < 10**6 and y+yy >= 0 and y+yy < 10**6 and (x+xx,y+yy) not in s:
                    queue.append([x+xx,y+yy])
                    s.add((x+xx,y+yy))
            
        return False
