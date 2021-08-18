class Solution:
    def isEscapePossible(self, blocked: List[List[int]], source: List[int], target: List[int]) -> bool:
        blocked = set(map(tuple, blocked))

        def dfs(x, y, sink, visited):
            if not (0 <= x < 10**6 and 0 <= y < 10**6) or (x, y) in blocked or (x, y) in visited:
                return False

            visited.add((x, y))
            if len(visited) > 20000 or [x, y] == sink:
                return True
            return dfs(x + 1, y, sink, visited) or dfs(x - 1, y, sink, visited) or dfs(x, y + 1, sink, visited) or dfs(x, y - 1, sink, visited)

        return dfs(source[0], source[1], target, set()) and dfs(target[0], target[1], source, set())
