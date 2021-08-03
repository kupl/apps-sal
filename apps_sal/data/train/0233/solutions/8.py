class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:

        N = len(grid)
        base = N * (N + 1)
        parent = [i for i in range(2 * base)]

        def find(x):
            if parent[x] != parent[parent[x]]:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            parent[find(x)] = find(y)
            return find(y)

        for i in range(N):
            for j in range(N):
                up, down, left, right = i * N + j, (i + 1) * N + j, base + i * (N + 1) + j, base + i * (N + 1) + j + 1

                if grid[i][j] == '/':
                    union(up, left)
                    union(down, right)
                elif grid[i][j] == '\\\\':
                    union(up, right)
                    union(down, left)
                else:
                    union(up, left)
                    union(down, right)
                    union(left, right)

        comp = set()
        for i in range(2 * base):
            comp.add(find(i))

        return len(comp)
