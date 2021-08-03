class Solution:
    def containsCycle(self, grid: List[List[str]]) -> bool:
        disjoint = {}

        def find(x):
            while disjoint[x] != x:
                x = disjoint[x]
            return disjoint[x]

        def union(x, y):
            disjoint[find(y)] = find(x)
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                disjoint[(i, j)] = (i, j)
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                for di, dj in [[0, 1], [1, 0]]:
                    if 0 <= i + di < len(grid) and 0 <= j + dj < len(grid[0]) and grid[i][j] == grid[i + di][j + dj]:
                        if find((i, j)) == find((i + di, j + dj)):
                            return True
                        union((i, j), (i + di, j + dj))
        return False
