class Solution:
    def knightDialer(self, n: int) -> int:
        Mod = 10**9 + 7
        dirs = [(-2, -1), (-2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2), (2, -1), (2, 1)]
        dp = [[1] * 3 for _ in range(4)]
        dp[3][0] = 0
        dp[3][2] = 0

        for k in range(1, n):
            temp = [[0] * 3 for _ in range(4)]
            for i in range(4):
                for j in range(3):
                    if i == 3 and j != 1:
                        continue
                    for x, y in dirs:
                        nx = i + x
                        ny = j + y
                        if nx < 0 or nx >= 4 or ny < 0 or ny >= 3:
                            continue
                        temp[i][j] = (temp[i][j] + dp[nx][ny]) % Mod
            dp = temp[:]

        print(dp)
        ans = 0
        for i in range(4):
            for j in range(3):
                ans = (ans + dp[i][j]) % Mod
        return ans
