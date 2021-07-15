import collections

class Solution:
    def isEscapePossible(self, blocked: List[List[int]], source: List[int], target: List[int]) -> bool:
        if not blocked: 
            return True
         
        blocked = set(map(tuple, blocked)) 
        print(len(blocked))
        
        return self.bfs(blocked, source, target) and self.bfs(blocked, target, source)
        
    def bfs(self, blocked, source, target):
        si, sj = source
        ti, tj = target
        
        queue = collections.deque([(si, sj)])
        visited = set()
        
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        step = 0
        while queue:
            size = len(queue)
            for _ in range(size):
                curX, curY = queue.popleft() 
                 
                if curX == ti and curY == tj:
                    return True
                
                for dx, dy in directions:
                    newX = curX + dx
                    newY = curY + dy
                    if self.isValid(newX, newY, blocked, visited):
                        queue.append((newX, newY))
                        visited.add((newX, newY))
            step += 1
            if step == len(blocked):
                break
                
        else:
            return False
        
        return True 
        
    def isValid(self, newX, newY, blocked, visited):
        return 0 <= newX < 1000000 and  0 <= newY < 1000000 and (newX, newY) not in blocked and (newX, newY) not in visited
