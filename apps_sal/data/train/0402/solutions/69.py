from collections import deque


class Solution:

    def isEscapePossible(self, blocked: List[List[int]], source: List[int], target: List[int]) -> bool:
        if not blocked or not blocked[0]:
            return True
        blocked = set(map(tuple, blocked))
        return self.bfs(tuple(source), tuple(target), blocked) and self.bfs(tuple(target), tuple(source), blocked)

    def bfs(self, source, target, blocked):
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        queue = deque([source])
        visited = set([source])
        while queue:
            (x, y) = queue.popleft()
            for (dx, dy) in directions:
                (x_, y_) = (x + dx, y + dy)
                if 0 <= x_ < 10 ** 6 and 0 <= y_ < 10 ** 6 and ((x_, y_) not in visited) and ((x_, y_) not in blocked):
                    if x_ == target[0] and y_ == target[1]:
                        return True
                    queue.append((x_, y_))
                    visited.add((x_, y_))
            if len(visited) > 20000:
                return True
        return False
