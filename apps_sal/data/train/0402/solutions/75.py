import collections

class Solution:
    def isEscapePossible(self, blocked: List[List[int]], source: List[int], target: List[int]) -> bool:
        if not blocked: 
            return True
         
        blocked = set(map(tuple, blocked))
        
        
        return self.bfs(blocked, source, target) and self.bfs(blocked, target, source)
        
    def bfs(self, blocked, source, target):
        si, sj = source
        ti, tj = target
        
        queue = collections.deque([(si, sj)])
        visited = set()
        
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        level = 0
        while queue:
            size = len(queue)
            for _ in range(size):
                curX, curY = queue.popleft()
                
                 
                if curX == ti and curY == tj:
                    return True
                
                for dx, dy in directions:
                    newX = curX + dx
                    newY = curY + dy
                    if 0 <= newX < 1000000 and  0 <= newY < 1000000 and (newX, newY) not in blocked and (newX, newY) not in visited:
                        queue.append((newX, newY))
                        visited.add((newX, newY))
            level += 1
            if level == len(blocked):
                break
                
        else:
            return False
        return True

