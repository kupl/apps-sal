class Solution:

    def isEscapePossible(self, blocked, source, target):
        blocked = {tuple(p) for p in blocked}
        directions = {(0, 1), (1, 0), (-1, 0), (0, -1)}

        def bfs(source, target):
            (queue, seen) = ([source], {tuple(source)})
            for (x0, y0) in queue:
                for (i, j) in directions:
                    (x, y) = (x0 + i, y0 + j)
                    if 0 <= x < 10 ** 6 and 0 <= y < 10 ** 6 and ((x, y) not in seen) and ((x, y) not in blocked):
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
        rows = cols = 10 ** 6
        directions = {(0, 1), (0, -1), (1, 0), (-1, 0)}
        (q1, q2) = ([tuple(source)], [tuple(target)])
        seen = set()
        blocked = {tuple(p) for p in blocked}
        while q1:
            next_q = []
            while q1:
                (r, c) = q1.pop()
                for (dr, dc) in directions:
                    if 0 <= r + dr < rows and 0 <= c + dc < cols and ((r + dr, c + dc) not in blocked) and ((r + dr, c + dc) not in seen):
                        if (r + dr, c + dc) in q2 or [r + dr, c + dc] == target:
                            return True
                        next_q.append((r + dr, c + dc))
                        seen.add((r + dr, c + dc))
            q1 = next_q
            if len(q1) > len(q2):
                (q1, q2) = (q2, q1)
        return False
