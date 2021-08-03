class Solution:
    def containsCycle(self, grid: List[List[str]]) -> bool:
        vis = [[False for i in range(len(grid[0]))] for j in range(len(grid))]

        dirx = [0, 0, -1, +1]
        diry = [-1, +1, 0, 0]

        def check(i, j):
            if 0 <= i < len(grid) and 0 <= j < len(grid[0]):
                return True
            return False

        def dfs(r, c, pr, pc, no):
            flag = False
            vis[r][c] = True
            for i in range(4):
                nr, nc = r + dirx[i], c + diry[i]
                if not (nr == pr and nc == pc) and check(nr, nc) and grid[nr][nc] == grid[r][c]:
                    if vis[nr][nc]:
                        print((nr, nc))
                        return True
                    if dfs(nr, nc, r, c, no + 1):
                        return True
            return False

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if not vis[i][j]:
                    if(dfs(i, j, -1, -1, 0)):
                        return True
        return False
