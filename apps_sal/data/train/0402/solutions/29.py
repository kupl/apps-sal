class Solution:
    def isEscapePossible(self, blocked: List[List[int]], source: List[int], target: List[int]) -> bool:

        # BFS
        blocked = {tuple(p) for p in blocked}

        def bfs(source, target):
            bfs, seen = [source], {tuple(source)}
            for x0, y0 in bfs:
                for i, j in [[0, 1], [1, 0], [-1, 0], [0, -1]]:
                    x, y = x0 + i, y0 + j
                    if [x, y] == target:
                        return True
                    if len(bfs) == 20000:
                        return True
                    if 0 <= x < 10**6 and 0 <= y < 10**6 and (x, y) not in seen and (x, y) not in blocked:
                        bfs.append([x, y])
                        seen.add((x, y))

            return False
        return bfs(source, target) and bfs(target, source)


# DFS
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
