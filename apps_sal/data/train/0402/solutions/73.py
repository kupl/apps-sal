class Solution:
    def isEscapePossible(self, blocked: List[List[int]], source: List[int], target: List[int]) -> bool:
        if not blocked:
            return True
        blocked = set(map(tuple, blocked))

        def bfs(start: list, final: list):
            seen, stack = {tuple(start)}, [start]
            for x, y in stack:
                for nx, ny in ((x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)):
                    if 0 <= nx < 10 ** 6 and 0 <= ny < 10 ** 6 and (nx, ny) not in seen and (nx, ny) not in blocked:
                        if [nx, ny] == final:
                            return True
                        seen.add((nx, ny))
                        stack.append((nx, ny))
                if len(stack) == 20000:
                    return True
            return False

        return bfs(source, target) and bfs(target, source)
