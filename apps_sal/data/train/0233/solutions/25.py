class Solution:

    def regionsBySlashes(self, grid: List[str]) -> int:
        N = len(grid)
        matrix = grid
        parent = list(range(N * N * 4))

        def find(x):
            depth = 0
            while parent[x] != x:
                x = parent[x]
                depth += 1
            return (x, depth)

        def union(x, y):
            ((rx, dx), (ry, dy)) = (find(x), find(y))
            if dx < dy:
                parent[rx] = ry
            else:
                parent[ry] = rx

        def isValid(i, j):
            if i >= N or i < 0 or j >= N or (j < 0):
                return False
            return True
        for i in range(N):
            for j in range(N):
                idtop = (i * N + j) * 4
                if matrix[i][j] == '/':
                    union(idtop + 1, idtop + 2)
                    union(idtop, idtop + 3)
                elif matrix[i][j] == '\\\\':
                    union(idtop, idtop + 1)
                    union(idtop + 2, idtop + 3)
                else:
                    union(idtop, idtop + 1)
                    union(idtop, idtop + 2)
                    union(idtop, idtop + 3)
                if isValid(i - 1, j):
                    union(idtop, 4 * ((i - 1) * N + j) + 2)
                if isValid(i, j - 1):
                    union(idtop + 3, 4 * (i * N + j - 1) + 1)
        return sum((find(x)[0] == x for x in range(4 * N * N)))
