import collections

class Solution:
    def isEscapePossible(self, blocked: List[List[int]], source: List[int], target: List[int]) -> bool:
        if not blocked: 
            return True
         
        blocked = set(map(tuple, blocked)) 
        # for b in blocked:
        #     block.add((b[0], b[1]))
        
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
    
    
    
    
    
    
#     def isEscapePossible(self, blocked, source, target):
#         blocked = {tuple(p) for p in blocked}

#         def bfs(source, target):
#             bfs, seen = [source], {tuple(source)}
#             for x0, y0 in bfs:
#                 for i, j in [[0, 1], [1, 0], [-1, 0], [0, -1]]:
#                     x, y = x0 + i, y0 + j
#                     if 0 <= x < 10**6 and 0 <= y < 10**6 and (x, y) not in seen and (x, y) not in blocked:
#                         if [x, y] == target: return True
#                         bfs.append([x, y])
#                         seen.add((x, y))
#                 if len(bfs) == 20000: return True
#             return False
#         return bfs(source, target) and bfs(target, source)


