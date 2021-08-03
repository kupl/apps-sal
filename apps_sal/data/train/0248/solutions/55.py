

class Solution:
    def containsCycle(self, grid: List[List[str]]) -> bool:
        n, m = len(grid), len(grid[0])
        root = {(i, j): (i, j) for i in range(n) for j in range(m)}

        def find(x):
            i, j = x
            if root[i, j] == x:
                return x
            root[i, j] = find(root[i, j])
            return root[i, j]

        def union(a, b):
            ra, rb = find(a), find(b)
            if ra != rb:
                root[rb] = ra
                return False
            return True

        for i in range(n):
            for j in range(m):
                val = grid[i][j]
                if i > 0 and grid[i][j] == grid[i - 1][j]:
                    union((i - 1, j), (i, j))
                if j > 0 and grid[i][j] == grid[i][j - 1]:
                    if union((i, j - 1), (i, j)):
                        return True
        return False
