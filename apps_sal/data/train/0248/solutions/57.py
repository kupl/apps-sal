class Solution:

    def containsCycle(self, grid: List[List[str]]) -> bool:
        (n, m) = (len(grid), len(grid[0]))
        root = {(i, j): (i, j) for i in range(n) for j in range(m)}

        def find(x):
            if root[x] == x:
                return x
            root[x] = find(root[x])
            return root[x]

        def union(a, b):
            (ra, rb) = (find(a), find(b))
            if ra != rb:
                root[ra] = rb
                return False
            return True
        for i in range(n):
            for j in range(m):
                val = grid[i][j]
                for (ni, nj) in [(i + 1, j), (i, j + 1)]:
                    if ni < n and nj < m and (grid[ni][nj] == val):
                        t = union((ni, nj), (i, j))
                        if t:
                            return True
        return False
