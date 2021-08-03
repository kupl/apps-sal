class Solution:
    def isEscapePossible(self, blocked: List[List[int]], source: List[int], target: List[int]) -> bool:
        blocked = set(map(tuple, blocked))

        def inbounds(x, y):
            return (x >= 0 and x < 10**6 and y >= 0 and y < 10**6)

        def dfs(x, y, target, seen):
            if (x, y) in blocked or not inbounds(x, y) or (x, y) in seen:
                return False
            seen.add((x, y))

            if len(seen) > 30000 or [x, y] == target:
                return True

            return dfs(x + 1, y, target, seen) or dfs(x - 1, y, target, seen) or dfs(x, y + 1, target, seen) or dfs(x, y - 1, target, seen)
            if not (0 <= x < 10**6 and 0 <= y < 10**6) or (x, y) in blocked or (x, y) in seen:
                return False
        return dfs(source[0], source[1], target, set()) and dfs(target[0], target[1], source, set())
