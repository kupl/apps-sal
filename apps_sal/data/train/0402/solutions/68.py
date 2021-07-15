from collections import deque
class Solution:
    def isEscapePossible(self, blocked: List[List[int]], source: List[int], target: List[int]) -> bool:
        if not blocked or not blocked[0]:
            return True
        
        blocked = set(map(tuple, blocked))
        print(blocked)
        return self.bfs(tuple(source), tuple(target), blocked) and self.bfs(tuple(target), tuple(source), blocked)
        
        
        
    def bfs(self, source, target, blocked):
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        
        queue = deque([source])
        
        visited = set([source])
        
        while queue:
            x, y = queue.popleft()
            for (dx, dy) in directions:
                x_ , y_ = x + dx, y + dy
                if 0 <= x_ < 10 ** 6 and 0 <= y_ < 10 ** 6 and (x_, y_) not in visited and (x_, y_) not in blocked:
                    if x_ == target[0] and y_ == target[1]:
                        return True
                    queue.append((x_, y_))
                    visited.add((x_, y_))
            if len(visited) > 20000:
                return True
        return False
    
                    
                 
        
        
        
        
        
        
        
        
        
        
#     def isEscapePossible(self, blocked, source, target):
#         blocked = set(map(tuple, blocked))

#         def dfs(x, y, target, seen):
#             if not (0 <= x < 10**6 and 0 <= y < 10**6) or (x, y) in blocked or (x, y) in seen: return False
#             seen.add((x, y))
#             if len(seen) > 20000 or [x, y] == target: return True
#             return dfs(x + 1, y, target, seen) or \\
#                 dfs(x - 1, y, target, seen) or \\
#                 dfs(x, y + 1, target, seen) or \\
#                 dfs(x, y - 1, target, seen)
#         return dfs(source[0], source[1], target, set()) and dfs(target[0], target[1], source, set())
# Python, BFS:
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

