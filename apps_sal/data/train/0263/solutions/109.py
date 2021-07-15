class Solution:
    def knightDialer(self, n: int) -> int:
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
    
        '''
        1  2  3
        4  5  6
        7  8  9
        -1 0 -1
        
        def dfs(d, x, y):
            if d == n:
                ans.append()
            # check x, y
            x + 2, y + 1, y - 1
            x - 2, y + 1, y - 1
            y + 2, x + 1, x - 1
            y - 2, x + 1, x - 1
            (2, 1), (2, -1), (-2, 1), (-2, -1), (1, 2), (-1, 2), (1, -2), (-1, -2)
            dfs(d + 1, nx, ny)
        
        '''
#         def dfs(d, x, y):
#             nonlocal ans
#             if d == n:
#                 ans += 1
#                 return 
#             for dx, dy in directions:
#                 nx, ny = x + dx, y + dy
#                 if nx < 0 or nx > M - 1 or ny < 0 or ny > N - 1 or matrix[nx][ny] == -1:
#                     continue
#                 dfs(d + 1, nx, ny)
                    
#         matrix = [[1, 2, 3], 
#                   [4, 5, 6],
#                   [7, 8, 9],
#                   [-1, 0, -1]]
#         M, N = len(matrix), len(matrix[0])
#         directions = [(2, 1), (2, -1), (-2, 1), (-2, -1), (1, 2), (-1, 2), (1, -2), (-1, -2)]
#         ans = 0
#         for i in range(M):
#             for j in range(N):
#                 if matrix[i][j] != -1:
#                     dfs(1, i, j)
#         return ans % (10**9 + 7)

