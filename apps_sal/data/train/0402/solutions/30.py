class Solution:

    def isEscapePossible(self, blocked: List[List[int]], source: List[int], target: List[int]) -> bool:

        def bfs(start, is_source=True):
            queue = [start]
            pending = set({start})
            visited = set()
            while len(queue) > 0:
                temp = queue.pop(0)
                (x1, y1) = temp
                if temp == tuple(target) and is_source:
                    return True
                if temp == tuple(source) and (not is_source):
                    return True
                visited.add(temp)
                if len(visited) > len(blocked) ** 2 // 2:
                    return True
                pending.remove(temp)
                for (x, y) in [(x1 + 1, y1), (x1 - 1, y1), (x1, y1 + 1), (x1, y1 - 1)]:
                    if 0 <= x < 10 ** 6 and 0 <= y < 10 ** 6:
                        if (x, y) not in pending and (x, y) not in blocked and ((x, y) not in visited):
                            queue.append((x, y))
                            pending.add((x, y))
            return False
        blocked = list(map(tuple, blocked))
        return bfs(tuple(source), True) and bfs(tuple(target), False)
