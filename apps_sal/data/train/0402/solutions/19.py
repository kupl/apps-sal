class Solution:

    def isEscapePossible(self, blocked: List[List[int]], source: List[int], target: List[int]) -> bool:
        blocks = {tuple(b) for b in blocked}

        def bfs(start, end):
            (queue, used) = ([start], {tuple(start)})
            for (x, y) in queue:
                for (dx, dy) in [[-1, 0], [1, 0], [0, 1], [0, -1]]:
                    (nx, ny) = (x + dx, y + dy)
                    if 0 <= nx < 10 ** 6 and 0 <= ny < 10 ** 6 and ((nx, ny) not in blocks) and ((nx, ny) not in used):
                        if [nx, ny] == end:
                            return True
                        queue.append([nx, ny])
                        used.add((nx, ny))
                if len(queue) == 20000:
                    return True
            return False
        return bfs(source, target) and bfs(target, source)
