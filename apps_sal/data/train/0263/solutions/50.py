class Solution:
    def knightDialer(self, n: int) -> int:
        # # starting points have 10 possible locations
        # grid = [
        #     [1,2,3],
        #     [4,5,6],
        #     [7,8,9],
        #     [None,0,None]
        # ]
        # # DFS to search through all possibilities
        # X = len(grid)
        # Y = len(grid[0])
        # def dfs(x,y,remain,X=X,Y=Y,grid=grid):
        #     if x < 0 or x >= X or y < 0 or y >= Y or not grid[x][y] or remain == 0:
        #         return -1
        #     temp_step = 8
        #     temp_step += dfs(x-2,y+1,remain-1)
        #     temp_step += dfs(x-1,y+2,remain-1)
        #     temp_step += dfs(x+1,y+2,remain-1)
        #     temp_step += dfs(x+2,y+1,remain-1)
        #     temp_step += dfs(x+2,y-1,remain-1)
        #     temp_step += dfs(x+1,y-2,remain-1)
        #     temp_step += dfs(x-1,y-2,remain-1)
        #     temp_step += dfs(x-2,y-1,remain-1)
        #     self.step *= temp_step
        #     print(temp_step)
        #     return temp_step
        # total = 0
        # for i in range(X):
        #     for j in range(Y):
        #         if grid[i][j]:
        #             self.step = 0
        #             dfs(i,j,n)
        #             total += self.step
        # return total % (10**9+7)
        MOD = 10**9 + 7
        moves = [[4,6],[6,8],[7,9],[4,8],[3,9,0],[],
                     [1,7,0],[2,6],[1,3],[2,4]]

        dp = [1] * 10
        for hops in range(n-1):
            dp2 = [0] * 10
            for node, count in enumerate(dp):
                for nei in moves[node]:
                    dp2[nei] += count
                    dp2[nei] %= MOD
            dp = dp2
        return sum(dp) % MOD
