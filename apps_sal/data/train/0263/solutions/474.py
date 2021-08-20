class Solution:

    def knightDialer(self, N: int) -> int:
        dirs = [(2, 1), (1, 2), (2, -1), (1, -2), (-2, -1), (-1, -2), (-2, 1), (-1, 2)]
        dp = [[0 for j in range(N)] for i in range(10)]
        for num in range(10):
            dp[num][0] = 1
        for i in range(1, N):
            for num in range(10):
                if num == 0:
                    pos = (1, 3)
                else:
                    pos = ((num - 1) % 3, (num - 1) // 3)
                x = pos[0]
                y = pos[1]
                for d in dirs:
                    new_x = x - d[0]
                    new_y = y - d[1]
                    if new_x < 0 or new_x > 2 or new_y < 0 or (new_y > 3):
                        continue
                    if new_x == 0 and new_y == 3 or (new_x == 2 and new_y == 3):
                        continue
                    new_num = 0 if new_x == 1 and new_y == 3 else new_y * 3 + new_x + 1
                    dp[num][i] += dp[new_num][i - 1]
        res = 0
        for num in range(10):
            res += dp[num][N - 1]
        return res % (pow(10, 9) + 7)
