class Solution:
    def knightDialer(self, n: int) -> int:
        M = 4
        N = 3
        KMOD = 10 ** 9 + 7
        dp = [[1 for _ in range(N)] for _ in range(M)] # init as 1 for 0/1 hops
        dp[3][0] = dp[3][2] = 0
        directions = [(1, 2), (-1, -2), (1, -2), (-1, 2),
                      (2, 1), (-2, -1), (2, -1), (-2, 1), ]
        for _ in range(1, n): # starts from 1 hop
            cur = [[0 for _ in range(N)] for _ in range(M)] # cur init as 0
            for i in range(M):
                for j in range(N):
                    if i == 3 and (j == 0 or j == 2):
                        continue
                    for d in directions:
                        x = i + d[0]
                        y = j + d[1]
                        if 0 <= x < M and 0 <= y < N:
                            cur[i][j] += dp[x][y]
            dp = cur
        result = 0
        for i in range(M):
            for j in range(N):
                if i == 3 and (j == 0 or j == 2):
                    continue
                result += dp[i][j]
        return result % KMOD
