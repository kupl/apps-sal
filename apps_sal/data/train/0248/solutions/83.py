class Solution:
    def containsCycle(self, grid: List[List[str]]) -> bool:
        W, H = len(grid[0]), len(grid)

        parent = list(range(W * H))
        rank = [0] * (W * H)

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            px, py = find(x), find(y)
            if px != py:
                if rank[px] > rank[py]:
                    parent[py] = px
                elif rank[px] < rank[py]:
                    parent[px] = py
                else:
                    parent[px] = py
                    rank[py] += 1

        for x in range(H):
            for y in range(W):
                if x and y and grid[x][y] == grid[x - 1][y] == grid[x][y - 1] and find((x - 1) * W + y) == find(x * W + y - 1):
                    return True

                for dx, dy in [(0, -1), (-1, 0)]:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < H and 0 <= ny < W and grid[nx][ny] == grid[x][y]:
                        union(x * W + y, nx * W + ny)

        return False

    def containsCycle_dfs(self, grid: List[List[str]]) -> bool:
        W, H = len(grid[0]), len(grid)

        visited = [[0] * W for _ in range(H)]

        def search(x, y, target, px, py):
            nonlocal grid, W, H, visited

            visited[x][y] = 1

            for dx, dy in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < H and 0 <= ny < W and grid[nx][ny] == target:

                    if visited[nx][ny]:
                        if nx == px and ny == py:
                            continue
                        return True

                    if search(nx, ny, target, x, y):
                        return True

            return False

        for x in range(H):
            for y in range(W):
                if not visited[x][y]:
                    if search(x, y, grid[x][y], None, None):
                        return True

        return False
