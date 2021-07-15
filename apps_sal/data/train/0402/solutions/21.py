class Solution:
    def isEscapePossible(self, blocked: List[List[int]], source: List[int], target: List[int]) -> bool:
#         blocked_set = set([tuple(l) for l in blocked])
#         visited = set(tuple(source))
#         visited_block_set = set()
#         step = 0
        
#         directions = [(0,1),(1,0),(0,-1),(-1,0)]
#         cur_queue = [tuple(source)]
#         next_queue = []
#         while True:
    
#             for c in cur_queue:
#                 for d in directions:
#                     if c[0]+d[0] >= 0 and c[1]+d[1] >= 0 and (c[0]+d[0], c[1]+d[1]) not in visited and (c[0]+d[0], c[1]+d[1]) not in blocked_set:
#                         visited.add((c[0]+d[0], c[1]+d[1]))
#                         next_queue.append((c[0]+d[0], c[1]+d[1]))
#                         if (c[0]+d[0], c[1]+d[1]) == tuple(target):
#                             return True
#                     elif (c[0]+d[0], c[1]+d[1]) in blocked_set:
#                         visited_block_set.add((c[0]+d[0], c[1]+d[1]))
                        
#             step += 1
#             cur_queue = next_queue
#             next_queue = []
            
#             if not cur_queue or step > 200:
#                 break
        
#         if step == 201:
#             return True
#         return False

        blocked = {tuple(p) for p in blocked}

        def bfs(source, target):
            bfs, seen = [source], {tuple(source)}
            for x0, y0 in bfs:
                for i, j in [[0, 1], [1, 0], [-1, 0], [0, -1]]:
                    x, y = x0 + i, y0 + j
                    if 0 <= x < 10**6 and 0 <= y < 10**6 and (x, y) not in seen and (x, y) not in blocked:
                        if [x, y] == target: return True
                        bfs.append([x, y])
                        seen.add((x, y))
                if len(bfs) == 20000: return True
            return False
        return bfs(source, target) and bfs(target, source)
