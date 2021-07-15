class Solution:
    def containsCycle(self, grid: List[List[str]]) -> bool:
        m = len(grid)
        n = len(grid[0])
        visited = {}
        
        def dfs(i, j, k):
            c = i * n + j
            if c in visited:
                return k - visited[c] >= 4
            visited[c] = k
            a = grid[i][j]
            for di, dj in [[0, -1], [0, 1], [-1, 0], [1, 0]]:
                ii = i + di
                jj =j + dj
                if not (0 <= ii < m and 0 <= jj < n) or grid[ii][jj] != a:
                    continue
                if dfs(ii, jj, k + 1):
                    return True
            return False
                
                
        for i in range(m):
            for j in range(n):
                c = i * n + j
                if c in visited:
                    continue
                if dfs(i, j, 0):
                    return True
        return False

