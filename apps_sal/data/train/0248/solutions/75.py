class Solution:
    def containsCycle(self, grid: List[List[str]]) -> bool:
        # dfs, remember parent
        self.m, self.n = len(grid), len(grid[0])
        nei = [(0, 1), (0, -1),(-1, 0), (1, 0)]
        memo = set()
        def dfs(i, j, p):
            # print(i, j, p, memo)
            if (i, j) in memo: return True
            memo.add((i, j))
            for ne in nei:
                x, y = i + ne[0], j + ne[1]
                if 0 <= x < self.m and 0 <= y < self.n and (x, y) != p and grid[i][j] == grid[x][y]:
                    if dfs(x, y, (i, j)): return True
            return False
            
        for i in range(self.m):
            for j in range(self.n):
                if (i, j) not in memo:
                    if dfs(i, j, (-1, -1)): return True
        return False

