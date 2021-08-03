
# 1036. Escape a Large Maze

class Solution:
    def isEscapePossible(self, blocked, source, target):
        blocked = {tuple(p) for p in blocked}
        directions = {(0, 1), (1, 0), (-1, 0), (0, -1)}

        def bfs(source, target):
            queue, seen = [source], {tuple(source)}
            for x0, y0 in queue:
                for i, j in directions:
                    x, y = x0 + i, y0 + j
                    if 0 <= x < 10**6 and 0 <= y < 10**6 and (x, y) not in seen and (x, y) not in blocked:
                        if [x, y] == target:
                            return True
                        queue.append([x, y])
                        seen.add((x, y))
                if len(queue) == 20000:
                    return True
            return False

        return bfs(source, target) and bfs(target, source)


class Solution1:
    def isEscapePossible(self, blocked: List[List[int]], source: List[int], target: List[int]) -> bool:

        if not blocked:
            return True

        rows = cols = 10**6
        directions = {(0, 1), (0, -1), (1, 0), (-1, 0)}
        q1, q2 = [tuple(source)], [tuple(target)]
        seen = set()
        blocked = {tuple(p) for p in blocked}

        while q1:
            next_q = []
            # current level
            while q1:
                r, c = q1.pop()
                # print(r, c, q1)
                for dr, dc in directions:
                    if 0 <= r + dr < rows and 0 <= c + dc < cols and (r + dr, c + dc) not in blocked and (r + dr, c + dc) not in seen:
                        if (r + dr, c + dc) in q2 or [r + dr, c + dc] == target:
                            return True
                        next_q.append((r + dr, c + dc))
                        seen.add((r + dr, c + dc))

            q1 = next_q
            if len(q1) > len(q2):
                q1, q2 = q2, q1

        return False


# class Solution:
#     def isEscapePossible(self, blocked: List[List[int]], source: List[int], target: List[int]) -> bool:

#         block = set()
#         for b in blocked:
#             block.add((b[0], b[1]))

#         directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
#         def dfs(sx, sy, tx, ty, cx, cy, visited):
#             if cx == tx and cy == ty:
#                 return True
#             if (abs(sx - cx) + abs(sy - cy)) > 200:
#                 return True
#             visited.add((cx, cy))
#             for d in directions:
#                 r = cx + d[0]
#                 c = cy + d[1]

#                 if r >= 0 and r < 1000000 and c >=0 and r < 1000000:
#                     if (r,c) not in block and (r, c) not in visited:
#                         if  dfs(sx, sy, tx, ty, r, c, visited):
#                             return True
#             return False
#         v1 = set()
#         v2 = set()
#         r1 = dfs(source[0], source[1], target[0], target[1], source[0], source[1], v1)
#         r2 = dfs(target[0], target[1], source[0], source[1], target[0], target[1], v2)
#         return r1 and  r2
