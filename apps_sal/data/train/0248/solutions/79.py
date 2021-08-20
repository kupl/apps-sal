class Solution:

    def containsCycle(self, grid: List[List[str]]) -> bool:
        visited = set()

        def dfs(x, y, parent):
            if (x, y) in visited:
                return True
            visited.add((x, y))
            c = grid[x][y]
            for (dx, dy) in [[0, -1], [0, 1], [-1, 0], [1, 0]]:
                (nx, ny) = (dx + x, dy + y)
                if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]) and (grid[nx][ny] == c) and ([nx, ny] != parent):
                    if dfs(nx, ny, [x, y]):
                        return True
            return False
        for x in range(len(grid)):
            for y in range(len(grid[0])):
                if (x, y) not in visited and dfs(x, y, [-1, -1]):
                    return True
        return False
